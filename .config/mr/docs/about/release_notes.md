# Release notes

## v1.1.3

Update mkdocs config for material 6.x. Mainly change value of key features in
mkdocs.yml

## v1.1.2

Move jinja_macros into _data and update mkdocs.yml accordingly.

## v1.1.1

Update requirements.in and requirements.txt to use the new plugin used to use
jinja macro in mkdocs.

Rename extra variable file from `_data/myrepos.yaml` to `_data/vars.yaml`.

## v1.1.0

Huge rework of the documentation to be render locally and to be included
using monorepo in docs.romaindeville.fr.

Thus leading to removing lots of assets and now redundant pages and updating CI.

## v1.0.4

Update link from framagit/myrepo to framagit/myrepos due to repo link update.

## v1.0.3

Minor update to fix upload of dev docs in CI.

## v1.0.2

Minor update, just change the output path to rsync when doing CI dev.

## v1.0.1

Empty release to trigger initial CI.

## v1.0.0

First release of **Myrepo Template** repo with scripts examples and
documentation.

Introduce a simple scripts (which could be improved) to semi-automatically setup
`myrepo` for a bunch of version control repos from a simple YAML config file.
