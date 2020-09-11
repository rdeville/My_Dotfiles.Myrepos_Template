# Direnv

## Description

From [Direnv][direnv]:

> direnv is an extension for your shell. It augments existing shells with a new
> feature that can load and unload environment variables depending on the current
> directory.

In other terms, when entering a directory configured to used direnv, a bash
script will be automatically executed allowing you to automate process such as
activating python virtual environment, settings environment variable only when
in the folder, etc.

Direnv already has a [online documentation][direnv] and also a manual (see `man
direnv` in your terminal) which describe its basic usage.

**Direnv is not required to be used with this repository but is recommended to
allow provided automation process**

## Usage

Basically, once the package and the hook is installed, when entering a folder in
in which there is a `.envrc` file, this `.envrc` file will automatically be
executed. When leaving the directory, any exported environment variable will
automatically be unset.

The folder `~/.config/mr/` has an `.envrc` file to automate the installation and
the activation of python virtual environment to be able to use the script
`~/.config/mr/main.py`.

If you have installed the package and the hook, when entering the folder you
should see the following message:

```
direnv: error ~/.config/mr/.envrc is blocked. Run `direnv allow` to approve its content
```

This is normal, direnv has a protection mechanism to only execute allowed
`.envrc`. Imaging cloning a repo where the file `.envrc` content is simply `sudo
rm -rf /`, without protection mechanism, you will lose your computer...

You can then review the described file to approve its content. **Be sure to
understand what this script do as well as every sourced scripts from it before
allowing it**.

Once you are confident in the behaviour of the script, you can allowing it with
the following command:

```
# Assuming you are in a folder which have an `.envrc` file
direnv allow
```

And that is all, now, unless the file `.envrc` is modified, each times you enter
the folder, the script `.envrc` will be executed.

[direnv]: https://direnv.net/
