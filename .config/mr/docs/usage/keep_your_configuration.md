z Keep your own configuration

## Initialize vcsh repo

Now that you have setup your configuration to use myrepos, you may want to keep
track of your configuration.

Normally, you should have following files to version:

  * Your YAML configuration files.
  * Your repos configuration files setup to be used by myrepos for each repos.
   Normally, these should be in the folder `repos` next to your YAML
   configuration file.
  * Your hosts configuration files setup defining which repos to manage with
   `myrepos` for your current host. Normally, theses files are in
   `~/.config/mr/hosts`

As an example, we will assume your YAML configuration file is
`~/.config/mr/perso/config.yaml`. Thus, your repos configurations files are in
`~/.config/mr/perso/repos/`. And finally, you host configuration file
`~/.config/mr/hosts/$(hostname).cfg`

To easily keep track of these and to be able to version them, the easiest way is
to use [vcsh][vcsh].

First initialize an empty vcsh repo:

```bash
# Initialize vcsh repo to store your configuraion
vcsh init myrepos_config
```

Then you have two possibilities:

  * Use `vcsh` git command directly
  * Activate `vcsh` shell to use git command normally

### Use `vcsh` git command

To use the `vcsh` git command, simply use it as follow:

```bash
# Replace <git command> with git command like add, commit, etc.
vcsh myrepos_config <git command>
```

For instance:

```bash
# First let us add our configuration file:
vcsh myrepos_config add ~/.config/mr/hosts/$(hostname).cfg
vcsh myrepos_config add ~/.config/mr/perso/repos/
vcsh myrepos_config add ~/.config/mr/perso/config.yaml
# Next commit it
vcsh myrepos_config commit
# This will prompt you your favorite editor to enter your commit message
```

Finally, let us upload your configuration to an online git platform:

```bash
# Add the origin remote
vcsh myrepos_config remote add origin git@git.platform.tld:namespace/myrepos_config.git
# Push our configuration files and set origin as upstream
vcsh myrepos_config push -u origin master
```

And that is all, now go to [Get your configuration files][get_config_file]
section to use it on another computer or if you reinstall your computer.

### Activate `vcsh` shell

Another way to do, if you are not pleasant with `vcsh` git command is to
activate `vcsh` shell. Once activated, you will be within your `vcsh` git repos
allowing you to use normal git command. To do so, simply type the following
command:

```bash
# Activate vcsh shell
vcsh myrepos_config shell
```

Now your `vcsh` shell is activated, you can use git command normally to version
your configuration files:

```bash
# First let us add our configuration file:
git add ~/.config/mr/hosts/$(hostname).cfg
git add ~/.config/mr/perso/repos/
git add ~/.config/mr/perso/config.yaml
# Next commit it
git commit
# This will prompt you your favorite editor to enter your commit message
```

Finally, let us upload your configuration to an online git platform:

```bash
# Add the origin remote
git remote add origin git@git.platform.tld:namespace/myrepos_config.git
# Push our configuration files and set origin as upstream
git push -u origin master
```

And that is all, now go to [Get your configuration files][get_config_file]
section to use it on another computer or if you reinstall your computer.

## Get your configuration files

Finally, to get your connfiguration files on another computer, you can simply
use `vcsh` to clone your online git repo. This will automatically put your
configuration files in the right place:

```bash
# Clone vcsh repo
vcsh clone git@git.platform.tld:namespace/myrepos_config.git myrepos_config
```

[vcsh]: https://github.com/RichiH/vcsh
[get_config_file]: #get-your-configuration-files
