# Setup myrepos configuration



<!-- vim-markdown-toc -->
To use this repository and mainly the script `~/.config/mr/main.py` you will
need to:

  - [Describe version control repository][describe_version_control_repo] you
   want to manage with myrepos.
  - [Generate per repos configuration][generate_per_repo_config] in myrepos
   format.
  - [Generate per host configuration][generate_per_host_config] to specify repos
   to be managed for the current hosts.

## Describe version control repository

Within the folder `~/.config/mr` create the YAML configuration file you will
provide to the script. The configuration will describe version control repos you
want to use with [myrepos][myrepos].

This file can be anywhere within `~/.config/mr` or in any subfolder and can have
any name. You can even crete two files, for instance:

  * `~/.config/mr/perso/config.yaml`, to store description of your personal
   repositories.
  * `~/.config/mr/pro/config.yaml`, to store description of your professionnal
   repositories.


Below is an example of the content of such configuration file:

```yaml
---
repos:
  # List of repos to be clone using vcsh
  vcsh:
      # Name of the repo for vcsh
    - name: myrepos
      # Description of the repo
      desc: MyRepos dotfiles configuration
      # HTTPS and/or  SSH remote URL
      remote:
        https: {{ git_platform.url }}{{ myrepos.namespace }}myrepos.git
        ssh: git@{{ git_platform.domain }}:{{ myrepos.namespace }}myrepos.git
      # Command to be run before or after the clone command
      command:
        # List of commands to be run before the clone of the repo
        pre_clone:
          - echo "Pre Clone command"
        # List of commands to be run after the clone of the repo
        post_clone:
          - echo "Initializing git flow after cloning the repo"
          - git flow init -d
  # List of repos to be clone using git
  git:
      # Name of the repo
    - name: st_dev
      # Path where the repo will be cloned
      path: ${HOME}/git/perso/private/forked_programs/st
      # Description of the repo
      desc: Development fork st suckless terminal
      # HTTPS and/or  SSH remote URL
      remote:
        https: {{ git_platform.url }}rdeville.private/my_forked_programs/st.git
        ssh: git@{{ git_platform.domain }}:rdeville.private/my_forked_programs/st.git
      # Command to be run before or after the clone command
      command:
        # List of commands to be run before the clone of the repo
        pre_clone:
          - echo "Pre Clone command"
        # List of commands to be run after the clone of the repo
        post_clone:
          - echo "Initializing git flow after cloning the repo"
          - git flow init -d
```


## Generate per repos configuration

Let us assume you put the configuration file in
`~/.config/mr/perso/my_config.yaml`. Now, generate a [myrepos][myrepos] file for
each of the version control repos describe in the configuration file.

```bash
# Assuming you are in ~/.config/mr and you install python dependencies
./main.py perso/my_config.yaml
# Or using absolute path or ${HOME} relative path
./main.py ~/.config/mr/perso/my_config.yaml
```

This will create the folder `~/.config/mr/perso/repos` in which there will be
configuration for each of the repos you specified in your configuration file.

If, like me, you want to configure multiple type of repos, some for personal
and other for professional repos, you can provide multiple configuration files at
once:

```bash
# Assuming you are in ~/.config/mr and you install python dependencies
./main.py perso/my_config.yaml pro/config.yaml
# Or using mixed of "absolute" path and relative path
./main.py ~/.config/mr/perso/my_config.yaml pro/config.yaml
```


This will create folder `~/.config/mr/perso/repos` and `~/.config/mr/pro/repos`
in which there will be configuration for each of the repos you specified in your
configuration files.



## Generate per host configuration

From the file `.mrconfig` at the root of this repo, you can configure multiple
hosts to be able to management multiple [myrepos][myrepos] configuration for
multiple hosts depending on the hostname.

Then you have two possibilities:

  - Manually configure your host
  - Using the script to interactively configure your host

### Manually configure host

If you want to manually configure repos managed with [myrepos][myrepos], first
create a the file `~/.config/mr/hosts/$(hostname).cfg` and add lines of the
forms:

```bash
# VCSH version controlled dotfiles
include = cat /path/to/repos/repo_name.vcsh
# Git version controlled repo
include = cat /path/to/repos/repo_name.git
```

Where `/path/to/repos` is the folder created next to your configuration file.

When configuring manually your host, you can also include all files within a
folder:

```toml
# Include all vcsh and git repos at once
include = cat /path/to/repos/*
```

### Automatically configure host

If you want, the script `main.py` has the option `-u` to automatically configure
the file `~/.config/mr/hosts/$(hostname).cfg`. Use this option when generating
version control configuration files:

```bash
# Assuming you are in ~/.config/mr using ~/.config/mr/perso/config.yaml
./main -u perso/config.yaml
```

After generating repository configuration files for [myrepos][myrepos], script
will prompt you a checkbox dialog to choose which repos you want to manage with
[myrepos][myrepos]. If you provide multiple configuration files, you will see
multiple checkbox dialog, once per configuration files provided to the script
`main.py`.

![!Repo List][checkbox_list_screenshot]

Red repos are classic git repo while green repos are vcsh repos. Once selected,
the file `~/.config/hosts/$(hostname).cfg` will automatically be created with
selected repos.

[describe_version_control_repo]: #describe-version-control-repository
[generate_per_repo_config]: #generate-per-repos-configuration
[generate_per_host_config]: #generate-per-host-configuration
[myrepos]: https://myrepos.branchable.com/
[checkbox_list_screenshot]: ../assets/img/checkbox_list.png
