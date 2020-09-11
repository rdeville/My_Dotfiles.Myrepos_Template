# Developers Guidelines

This document will describe main guidelines for developers who want to
contribute to this repo. It rely on other documentation in this repo for which
link will be provided when needed.

The aim of this document is to describe how to help development of this project,
how to properly contribute and provide a link the style code used in this repo.

Most of this guidelines are not mandatory, its mainly to make code and
documentation more homogenous and help people to understand what is done in the
code.

## Workflow

The repo use git flow branching model, for more information see:

  * [A successful git branching model][git_branching_model].

To help you following this branching model, you can use `git flow` command. To
install this command, see:

  * [git flow][git_flow] to install package
  * [git flow cheatsheet][git_flow_cheatsheet]

Branches should start with prefix `feature-`, `bugfix-`, `release-` and
`hotfix-`.

Except for the main developers `master`, `develop` and `release-` branches are
protected. You will not be able to push directly on these branches.

For now, main developpers are:

  * [ rdeville](https://framagit.org/rdeville)

## Tutorials

Let us do a little tutorial to apply this workflow.

This tutorial will follow the following workflow steps:

  1. Fork this repo (Optional),
  2. Setup your working environment,
  3. Create your working branch,
  4. Work on this branch,
  5. Ensure your modification are documented and pass the tests,
  6. Once finished and tested, your can merge this branch to your branch,
  7. Prepare your merge request,
  8. Propose a merge request on the main repo.

### 1. Fork this repo (Optional)

This step is optional, as you can work directly on the main repo by creating
branch corresponding on what you are working on like `feature-*` or `bugfix-*`.
But it is the prefered method if you want to keep your configuration and be free
to name the branch whatever you want.

### 2. Setup your working environment

First thing to do once the repo is cloned is to setup your working environment.

To do so, please refer to the section [Setup myrepos
configuration][setup_myrepos].

Next, we will assume you activate the `vcsh` shell, allowing to use classic git
command.

### 3. Create your working branch

In this exemple we will add a new documentation page, it is kind of a new
feature, so the new branch will be name `feature-doc-content-title`.

```bash
# Create the branch and directly go to it
git checkout -b feature-doc-content-title
```

**NOTE**: If it is a bufix, the branch name may be like
`bugfix-name-of-the-bug`, etc. This naming convention is only if you wish to
work directly on the main repo, you are free to name the branch whatever you
like on your own fork.

### 4. Work on this branch

Then, do the work you need to do on your branch.

  * If you want to write the documentation page and are new using mkdocs, a
    tutorials is provided to help you adding content to the documentation.

    See [Update documentation][update_documentation].

  * If you want to setup/modify the CI to automatically push the website, a
    tutorial is provided to help you learn how to do it.

    See [Update CI][update_ci].

### 5. Ensure your modification are documented and pass the tests

To ensure your modification are valid, i.e. pass the test, simply use the
following command:

```bash
# Assuming you are in ~/.config/mr and you setup python dev requirements
tox
```

This will automatically run the testing tools (also used in the CI) and will
ensure the build of the documentation:

* [tox][tox]: Setup python testing suite
* [shellcheck][shellcheck]: Shell script analysis tools
* [isort][isort]: Python import sorting
* [pylint][pylint]: Python linter
* [flake8][flake8]: Python syntax validator
* [black][black]: Python optionless formatter
* [pytest][pytest]: Python test tool

For more information, you can check following files:

* [pyproject.toml][pyproject]
* [.gitlab-ci.yaml][gitlab_ci]

### 6. Merge branch on your fork

This step is optional and only if you make a fork of the repo, otherwise, go
directly to the next section.

Now you have finish your work, you can merge this feature into your `develop` or
`master` branch (you are free of your branch management in your own fork).

```bash
# Go to your develop branch
git checkout develop
# Merge feature into develop
git merge feature-doc-content-title
```

!!! important
    If you did not make a fork of the repo, when merging your branch to `master`
    or `develop`, you will have no issues. But when pushing your modification,
    these modification will be rejected as branch `master` and `develop` are
    protected on the main repo.

### 7. Prepare your merge request

Before proposing your merge request, ensure that :

  - Your your configuration files are not versionned

### 8. Propose a merge request on the main repo

Finally, you can propose a merge request.

#### If you make a fork of the main repo

To do so, if your fork is not on [ framagit.org][gitlab], you may need to
push it on this platform.

To do so, create an account on [ framagit.org][gitlab] or ask your
colleague how to do so as [ framagit.org][gitlab] may not allow open
registration.

Then, create an empty repo on [ framagit.org][gitlab] and create the
remote on your local folder and push your repo:

```bash
git remote add upstream-fork https://framagit.org/<USER>/<REPO_NAME>
# To be sure, push all your branch, or if you know, push only needed branches
git push upstream-fork --all
```

Then propose your merge request on the branch `master` of the main repo. **DO
NOT FORGET TO BE EXPLICIT ON YOU MERGE REQUEST**

#### If you work directly on a branch on the main repo

You can direclty propose your merge request on the branch `master` of the main
repo. **DO NOT FORGET TO BE EXPLICIT ON YOU MERGE REQUEST**

[tox]: https://tox.readthedocs.io/en/latest/
[pylint]: https://pylint.org/
[isort]: https://timothycrosley.github.io/isort/
[black]: https://pypi.org/project/black/
[flake8]: https://pypi.org/project/flake8/
[pytest]: https://pypi.org/project/pytest/
[mkdocs]: https://pypi.org/project/mkdocs/
[shellcheck]: https://github.com/koalaman/shellcheck

[pyproject]: https://framagit.org/rdeville.private/my_dotfiles/myrepo/.config/mr/pyproject.toml
[gitlab_ci]: https://framagit.org/rdeville.private/my_dotfiles/myrepo/.config/mr/.gitlab_ci.yaml

[gitlab]: https://framagit.org
[git_branching_model]: https://nvie.com/posts/a-successful-git-branching-model/
[git_flow]: https://github.com/nvie/gitflow/wiki/Installation
[git_flow_cheatsheet]: https://danielkummer.github.io/git-flow-cheatsheet/

[setup_myrepos]: ../usage/setup_myrepos_configuration.md
[update_documentation]: tutorials/update_documentation.md
[update_ci]: tutorials/update_ci.md
