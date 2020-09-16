# Myrepos

## Description

From [myrepos documentation][myrepos_doc]:

> You have a lot of version control repositories. Sometimes you want to update
> them all at once. Or push out all your local changes. You use special command
> lines in some repositories to implement specific workflows. Myrepos provides a
> mr command, which is a tool to manage all your version control repositories.

In other terms, if you want to push all your version control repos configured,
you will just need the command `mr push`.

In this documentation, we will not document how to use myrepos as this is already
well described in the [online documentation][myrepos_doc] and in the manual of
the command (see `man mr` in your terminal). We will only describe usage
adaptation dones from the basic myrepos configuration.

## Adaptation

Normally, myrepos provide a `mr register` command to be run in a version control
repo. Normally, this command will automatically add your git repo in your
`~/.mrconfig` file.

This template repository does not rely on this command but take it the other
way. Thus the content of `~/.mrconfig` will not be updated as it will include
host configuration file. This host configuration file will then include the
repos configuration files you want to manage for you current host. Below is the
content of `~/.mrconfig`

```toml
[DEFAULT]
# Teach mr how to `mr gc` in git repos.
git_gc = git gc "$@"

include =
  if [ -f "${HOME}/.config/mr/hosts/$(hostname).cfg" ]
  then
    cat "${HOME}/.config/mr/hosts/$(hostname).cfg"
  fi
```

You will have to manually specify repos you want to manage with myrepos in
a YAML configuration file and use the script `main.py` at the root of the repos
to setup configuration. There is two set of configuration files:

  * Per repos configuration
  * Per host configuration

### Per repos configuration

From the YAML file provided as input of the `main.py` script, the script will
create a `repos` directory next to the YAML file in which it will store the `mr`
action for each repos describe in the YAML file.

Below is an example of such file for version control repositories managed with
git and [vcsh][vcsh].


??? info "Exemple of git repo configuration"

    Content of the YAML input for the repo:

    ```yaml
    repos:
      git:
        - name: st_prod
          path: ${HOME}/.local/src/st
          desc: Production fork st suckless terminal
          remote:
            https: {{ git_platform.url }}rdeville.public/my_forked_programs/st.git
            ssh: git@{{ git_platform.domain }}:rdeville.public/my_forked_programs/st.git
          command:
            post_clone:
              - git flow init -d
              - make
              - sudo make install
    ```

    Content of the outputed myrepo configuration:
    ```toml
    [${HOME}/.local/src/st]
    checkout  =
      echo '\e[0;32m[INFO] Clone st_prod from {{ git_platform.domain }}\e[0m'
      git clone git@{{ git_platform.domain }}:rdeville.public/my_forked_programs/st.git ${HOME}/.local/src/st
      cd ${HOME}/.local/src/st
      echo '\e[0;32m[INFO]    Set upstream push\e[0m'
      git push -u origin master;
      echo '\e[0;32m[INFO]    Pull all remote branch\e[0m'
      git pull --all;
      git flow init -d
      make
      sudo make install
    pull      =
      echo '\e[0;32m[INFO] Pull st_prod from {{ git_platform.domain }}\e[0m';
      git pull origin $(git branch --show-current) --all;
    update    =
      echo '\e[0;32m[INFO] Pull st_prod from {{ git_platform.domain }}\e[0m';
      git pull origin $(git branch --show-current) --all;
    push      =
      echo '\e[0;32m[INFO] Push all st_prod to {{ git_platform.domain }}\e[0m';
      git push --all;
      echo '\e[0;32m[INFO] Push tags st_prod to {{ git_platform.domain }}\e[0m';
      git push --tags;
    upstream  =
      echo '\e[0;32m[INFO] Setting upstream of st_prod to origin\e[0m';
      git branch --set-upstream-to=origin/$(git branch --show-current) $(git branch --show-current);
    remote    =
      git remote -v show;
    branch    =
      git branch -a;
    delete    =
      echo '\e[0;31m[WARNING} Will delete \e[1;31mst_prod.\e[0m';
      echo 'Press \e[0;31mEnter\e[0m to continue or \e[0;32mCtrl-D\e[0m to abort';
      read yn;
      echo '\e[0;31mDelete \e[1;31mst_prod\e[0;31m.\e[0m';
      rm -rf ${HOME}/.local/src/st;
    ```

??? info "Exemple of vcsh repo configuration"


    Content of the YAML input for the repo:

    ```yaml
    repo:
      vcsh:
        - name: myrepos
          desc: MyRepos main dotfiles configurations
          remote:
            https: {{ git_platform.url }}{{ myrepos.namespace }}{{ myrepos.name }}.git
            ssh: git@{{ git_platform.domain }}:{{ myrepos.namespace }}{{ myrepos.name }}.git
          command:
            post_clone:
              - git flow init -d
    ```

    Content of the outputed myrepo configuration:
    ```toml

    [${HOME}/.config/vcsh/repo.d/myrepos.git]
    checkout  =
      echo '\e[0;32m[INFO] Clone myrepos from {{ git_platform.domain }}\e[0m'
      vcsh clone git@{{ git_platform.domain }}:{{ myrepos.namespace }}{{ myrepos.name }}.git {{ myrepos.name }}
      echo '\e[0;32m[INFO]    Set upstream push\e[0m'
      vcsh myrepos push -u origin master;
      echo '\e[0;32m[INFO]    Pull all remote branch\e[0m'
      vcsh myrepos pull --all;
      echo 'git flow init -d; exit' |  vcsh myrepos
    pull      =
      echo '\e[0;32m[INFO] Pull myrepos from {{ git_platform.domain }}\e[0m';
      vcsh myrepos pull origin $(git branch --show-current) --all;
    update    =
      echo '\e[0;32m[INFO] Pull myrepos from {{ git_platform.domain }}\e[0m';
      vcsh myrepos pull origin $(git branch --show-current) --all;
    upstream  =
      echo '\e[0;32m[INFO] Setting upstream of myrepos to origin\e[0m';
      vcsh myrepos branch --set-upstream-to=origin/$(vcsh myrepos branch --show-current) $(vcsh myrepos branch --show-current);
    push      =
      echo '\e[0;32m[INFO] Push all myrepos to {{ git_platform.domain }}\e[0m';
      vcsh myrepos push --all;
      echo '\e[0;32m[INFO] Push tags myrepos to {{ git_platform.domain }}\e[0m';
      vcsh myrepos push --tags;
    remote    =
      vcsh myrepos remote -v show;
    branch    =
      vcsh myrepos branch -a;
    delete    =
      echo '\e[0;31m[WARNING] Will delete \e[1;31mmyrepos.\e[0m';
      echo 'Press \e[0;31mEnter\e[0m to continue or \e[0;32mCtrl-D\e[0m to abort';
      read yn;
      echo '\e[0;31mDelete \e[1;31mmyrepos\e[0;31m.\e[0m';
      vcsh delete myrepos;
    ```

Assuming the YAML configuration file is `perso/config.yaml` relative to the
`main.py` script, per repos configuration can be automatically generated with
the following command:

```bash
# Assuming you are at the root the repo
./main.py perso/config.yaml
```

This will create the folder `perso/repos` with per repos configuration in it.

### Per host configuration

Once per repos configuration files are generated, you will need to setup host
configuration files. This file is included as described in `~/.mrconfig`. It
should be located at `~/.config/mr/hosts/$(hostname).cfg`.

From there, you have to possibility:

  * [Manually configure host][manual_host_config]
  * [Automatically configure host][auto_host_config]

Below is an example content of such host configuration including the repos
configured in the previous section:

```toml
# VCSH version controlled dotfiles
include = cat ${HOME}/.config/mr/perso/myrepos.vcsh
# Git version controlled repo
include = cat ${HOME}/.config/mr/perso/st_dev.git
```

When configuring manually your host, you can also include all files within a
folder:

```toml
# Include all vcsh and git repos at once
include = cat ${HOME}/.config/mr/perso/*
```

[myrepos_doc]: https://myrepos.branchable.com/
[vcsh]: https://github.com/RichiH/vcsh
[manual_host_config]: ../usage/setup_myrepos_configuration.md#manually-configure-host
[auto_host_config]: ../usage/setup_myrepos_configuration.md#automatically-configure-host
