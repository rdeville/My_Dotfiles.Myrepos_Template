#!/usr/bin/env python3
"""
Script to automate configuration of myrepos.
"""

import argparse
import os
import socket
import sys
from datetime import date
from pathlib import Path

import giturlparse
import pykwalify
from jinja2 import Environment, FileSystemLoader
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import checkboxlist_dialog
from prompt_toolkit.styles import Style
from pykwalify import core as pykwalify_core

THIS_FILE_DIR = os.path.abspath(os.path.dirname(__file__))
"""The absolute path of the script"""
MR_DIR = os.path.join(os.environ["HOME"], ".config", "mr")
"""The absolute path of the myrepos folder"""
HOSTNAME = socket.gethostname()
"""The hostname of the current computer"""
HOST_FILE = os.path.join(MR_DIR, "hosts", HOSTNAME + ".cfg")
"""The absolute path where the host configuration will be stored"""
TODAY = date.today()
TODAY = TODAY.strftime("%Y-%m-%d")
"""Today date for backup file"""
CONFIG_SCHEMA = [os.path.join(MR_DIR, "config.schema.yaml")]
"""Absolute paths to the YAML schema"""


class Colors:
    """
    Simple class to store prefix string to color output.
    """

    # pylint: disable=too-few-public-methods
    info = "\033[32m"
    """Color prefix when printing info log, usually green"""
    warning = "\033[33m"
    """Color prefix when printing warning log, usually yellow"""
    error = "\033[31m"
    """Color prefix when printing error log, usually red"""
    normal = "\033[0m"
    """Color prefix to revert printing log back to normal"""
    bold = "\033[1m"
    """Color prefix print log in bold"""


class Repo:
    """
    Class which handle the configuration of repos for myrepos.
    """

    def __init__(self, conf_file: str, dest_dir: str) -> None:
        """
        Default constructor to initialize Repo object which will store:

          - Current LC_ALL and LANGUAGE environment variable
          - Setup destination directory where repo configuration will be stored
          - Configuration provided by user
          - Jinja2 information to render file from templates

        Arguments:
            conf_file: Path to the configuration file
            dest_dir:
                Path to the directory where myrepos configuration will be stored
        """
        self._env = dict()
        self._dest_dir = os.path.join(THIS_FILE_DIR, "repos", dest_dir)
        self._conf = load_config(conf_file)
        self._j2_file_loader = FileSystemLoader("templates")
        self._j2_env = Environment(loader=self._j2_file_loader)

        if "LC_ALL" in os.environ:
            self._env["LC_ALL"] = os.environ["LC_ALL"]
        if "LANGUAGE" in os.environ:
            self._env["LANGUAGE"] = os.environ["LANGUAGE"]
        os.environ["LC_ALL"] = "en_US.UTF-8"
        os.environ["LANGUAGE"] = "en_US.UTF-8"

    def __del__(self) -> None:
        """
        Default deleter which will restore environment variables LC_ALL and
        LANGUAGE
        """
        if "LC_ALL" in self._env:
            os.environ["LC_ALL"] = self._env["LC_ALL"]
        if "LANGUAGE" in self._env:
            os.environ["LANGUAGE"] = self._env["LANGUAGE"]

    def _process_single_repo(self, repo_type, repo):
        repo_name = repo["name"]
        if repo_type == "git":
            repo_path = repo["path"]
        elif repo_type == "vcsh":
            repo_path = ""
        if "ssh" in repo["remote"]:
            repo_url = repo["remote"]["ssh"]
        elif "https" in repo["remote"]:
            repo_url = repo["remote"]["https"]
        else:
            print("[ERROR] - No remote for git repo" + repo_name)
            exit_code(1)
        if "git_flow" in repo:
            git_flow = repo["git_flow"]
        else:
            git_flow = False
        repo_domain = giturlparse.parse(repo_url).resource
        command = dict()
        if "command" in repo:
            command = repo["command"]
        tpl = self._j2_env.get_template(repo_type + ".tpl.j2")
        out = tpl.render(
            repo_name=repo_name,
            repo_path=repo_path,
            repo_url=repo_url,
            repo_domain=repo_domain,
            git_flow=git_flow,
            command=command,
        )
        if not os.path.isdir(self._dest_dir):
            os.mkdir(self._dest_dir)
        outfile = os.path.join(self._dest_dir, repo_name + "." + repo_type)
        with open(outfile, "w") as fopen:
            print(out, file=fopen)

    def process(self) -> None:
        """
        Process the initialization of git and vcsh repos as defined in
        configuration file.
        """
        if "git" in self._conf["repos"]:
            for i_git_repo in self._conf["repos"]["git"]:
                self._process_single_repo("git", i_git_repo)
        if "vcsh" in self._conf["repos"]:
            for i_vcsh_repo in self._conf["repos"]["vcsh"]:
                self._process_single_repo("vcsh", i_vcsh_repo)


class Host(Repo):
    """
    Class which handle the update of host configuration. Inherit Repo Class
    Inherit Repo Class.
    """

    # pylint: disable=too-few-public-methods
    def _process_host_repos(self, repo_type, repos, values):
        if not os.path.isdir(self._dest_dir):
            os.mkdir(self._dest_dir)
        for i_repo in self._conf["repos"][repo_type]:
            key = os.path.join(self._dest_dir, i_repo["name"] + "." + repo_type)
            if repo_type == "git":
                style_1 = "#FF0000"
                style_2 = "#990000"
                path = i_repo["path"]
            elif repo_type == "vcsh":
                style_1 = "#00FF00"
                style_2 = "#009900"
                path = "${HOME}/.config/vcsh/repo.d/" + i_repo["name"]
            desc = (
                "<style fg='"
                + style_1
                + "'>"
                + i_repo["name"]
                + "\n      "
                + i_repo["desc"]
                + "\n      "
                + "</style>"
                "<style fg='" + style_2 + "'>" + path + "</style>"
            )
            values.append((key, HTML(desc)))
            repos[key] = i_repo["desc"]
        return values, repos

    def process(self) -> None:
        """
        Compute the dialog window to ask user which repos to setup for the
        current host
        """
        title = "Setup " + HOSTNAME
        text = "Which repo to setup with myrepo on " + HOSTNAME
        values = list()
        result_arrays = list()
        repos = dict()
        selected_repo = dict()
        style = Style.from_dict(
            {
                "dialog": "bg:#333333",
                "dialog frame.label": "bg:#ffffff #000000",
                "dialog.body": "bg:#000000 #DDDDDD",
                "dialog shadow": "bg:#333333",
                "checkbox-list": "#333333",
                "checkbox-checked": "#00FFFF",
                "checkbox-selected": "#FFFF00",
            }
        )

        if "git" in self._conf["repos"]:
            self._process_host_repos("git", repos, values)

        if "vcsh" in self._conf["repos"]:
            self._process_host_repos("vcsh", repos, values)

        values.append(("", ""))
        result_arrays = checkboxlist_dialog(
            title=title,
            text=text,
            values=values,
            style=style,
        ).run()

        if "" in result_arrays:
            result_arrays.remove("")
        if not result_arrays:
            return False

        for i_repo in result_arrays:
            selected_repo[i_repo] = repos[i_repo]

        tpl = self._j2_env.get_template("hosts.tpl.j2")
        out = tpl.render(selected_repo=selected_repo)
        with open(HOST_FILE, "a") as fopen:
            print(out, file=fopen)

        return True


def exit_code(return_code: int) -> None:
    """
    Method to print an error message before leaving the script with the provided
    return code

    Arguments:
        return_code: The return code of the script
    """
    if return_code != 0:
        print(
            Colors.error
            + "[ERROR] - Something went wrong. Installation aborted"
            + Colors.normal
        )
    sys.exit(return_code)


def load_config(filename: str) -> dict:
    """
    Ensure the provided configuration file is valid.

    Print an error if not else return the content of the configuration file.

    Arguments:
        filename: Path to the configuration file.

    Returns:
        The content of the configuration file.
    """
    check = pykwalify_core.Core(
        source_file=filename, schema_files=CONFIG_SCHEMA
    )
    try:
        check.validate(raise_exception=True)
    except pykwalify.errors.SchemaError as exc:
        print("ERROR - File " + filename + " does not respect schema files:")
        for i_schema in CONFIG_SCHEMA:
            print("ERROR -        - " + i_schema)
        print("ERROR - Errors are : ")
        for i_msg in exc.args:
            print(i_msg)
        sys.exit(1)
    return check.source


def compute_configs(config_files: str) -> dict:
    """
    Compute a dictionary which store the absolute path to the configuration file
    and the subdirectory from which the configuration file is loaded and where
    the repos will be stored.

    Arguments:
        config_files: Path to the configuration file

    Returns:
        A dictionary which store configuration file path and output directory.
    """
    configs = list()
    for i_files in config_files:
        parent = Path(i_files).parent
        if parent.is_absolute():
            configs.append(
                {
                    "dir": os.path.join(parent, "repos"),
                    "file": os.path.join(parent, i_files),
                }
            )
        else:
            configs.append(
                {
                    "dir": os.path.join(MR_DIR, parent, "repos"),
                    "file": os.path.join(MR_DIR, i_files),
                }
            )
    return configs


def process_repos(configs: dict) -> None:
    """
    Process configuration files to compute repos for myrepos.

    Arguments:
        configs: Dictionary which store configuration file path and output
        directory.
    """
    for i_config in configs:
        if os.path.isfile(i_config["file"]):
            print(
                Colors.info
                + "[INFO] - Processing file "
                + Colors.bold
                + i_config["file"]
                + Colors.normal
            )
            repo = Repo(i_config["file"], i_config["dir"])
            repo.process()
        else:
            print(
                Colors.error
                + "[ERROR] - File "
                + Colors.bold
                + i_config["file"]
                + Colors.normal
                + Colors.error
                + " does not exists"
                + Colors.normal
            )


def process_host(configs: dict) -> None:
    """
    Process configuration files to compute host configuration for myrepos.

    Arguments:
        configs: Dictionary which store configuration file path and output
        directory.
    """
    for i_config in configs:
        if os.path.isfile(i_config["file"]):
            print(
                Colors.info
                + "[INFO] - Processing file "
                + Colors.bold
                + i_config["file"]
                + Colors.normal
            )
            host = Host(i_config["file"], i_config["dir"])
            host.process()
        else:
            print(
                Colors.error
                + "[ERROR] - File "
                + Colors.bold
                + i_config["file"]
                + Colors.normal
                + Colors.error
                + " does not exists"
                + Colors.normal
            )


def backup_host_config() -> None:
    """
    Back the file `~/.config/mr/hosts/$(hostname).cfg` if it already exists.
    """
    print(
        Colors.info
        + "[INFO] Backup file "
        + Colors.bold
        + HOST_FILE
        + Colors.normal
    )
    os.rename(HOST_FILE, HOST_FILE + ".bak." + TODAY)


def parse_arg() -> dict:
    """
    Parse script input arguments.

    Returns:
        Dictionary storing arguments passed to the script.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u",
        "--update-config",
        action="store_true",
        dest="update_host",
        help="Update hosts configuration",
    )
    parser.add_argument(
        "config_files",
        nargs="+",
        type=str,
        action="append",
        metavar="FILE",
        help="Path to a configuration file",
    )
    return parser.parse_args()


def main() -> None:
    """
    Main method processing configuration file and generate myrepos configuration
    and hosts configuration.
    """
    arg = parse_arg()
    if arg.config_files[0]:
        configs = compute_configs(arg.config_files[0])
        process_repos(configs)
    if arg.update_host:
        if os.path.isfile(HOST_FILE):
            backup_host_config()
        process_host(configs)


if __name__ == "__main__":
    # execute only if run as a script
    main()
