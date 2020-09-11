# VCSH

## Description

From [ RichiH/vcsh][vcsh_repo_url]:

> vcsh - Version Control System for $HOME - multiple Git repositories in $HOME

In other terms, `vcsh` will allow to directly version files from your `$HOME`
without having a `.git` in your `$HOME`. Moreover, it also allow you to have
multiple git repositories which root is your `$HOME`. One of the main usages of
this program is to version your dotfiles without having to worrying about
symlinks or install scripts.

An example of such version repo is this current [myrepo
template][myrepo_template_url].

A quick usage description is provided in the README.md of [
RichiH/vcsh][vcsh_repo_url] and a more details usage description is provided
with the manual of the command (see `man vcsh` in your terminal).

## Usage

The command is used as it is in combination with [myrepo][myrepos_doc_url]. The
main advantage is you can gather all your dotfiles in very few simple git like
commands.

For instances, assuming you have following dotfiles repositories:

  - This current repository which hold config scripts
  - Your own myrepos vcsh base repository to store your own configuration (see
   [Keep your own configuration][keep_your_configuration])
  - Multiple vcsh and git based repositories described in your own configuration.

When installing a new computer, gathering all your `vcsh` and `git` based repos
is as simple as:

```bash
# First clone this current repository
vcsh clone https://framagit.org/rdeville.public/my_dotfiles/myrepo.git myrepo
# Seconf clone you own configuration
vcsh clone git@mygit.tld:namespace/myrepo_config.git
# Assuming that your personal configuratio is in ${HOME}/.config/mr/perso/
# Go where the script main.py is
cd ~/.config/mr
# Create python virtual environment
python3 -m venv .virtualenv
# Activate the virtual environment
source .virtualenv/bin/activate
# Install python required dependencies in the virtualenvironment
pip3 install -r requirements.txt
# Generate configuration for your computer
./main.py -u perso/config.yaml
# Let us got to the top level from where every vcsh and git repos will be clone
cd ~
# Finally, let us gather all your vcsh and git repos at once
mr checkout
```

Even better, if your repos and hosts are already configured in your own myrepos
configuration, commands will simply be:

```bash
# Assuming you are in your $HOME folder
# First clone this current repository
vcsh clone https://framagit.org/rdeville.public/my_dotfiles/myrepo.git myrepo
# Seconf clone you own configuration
vcsh clone git@mygit.tld:namespace/myrepo_config.git myrepo_perso
# Finally, let us gather all your vcsh and git repos at once
mr checkout
```


Last command will print a lots of output, this is normal as the command `mr
checkout` will automatically clone every configured repos which clone path is a
subfolder of your `$HOME`, including `vcsh` dotfiles.


[vcsh_repo_url]: https://github.com/RichiH/vcsh
[myrepo_template_url]: https://framagit.org/rdeville.public/my_dotfiles/myrepo
[myrepos_doc_url]: https://myrepos.branchable.com/
[keep_your_configuration]: ../usage/keep_your_configuration.md
