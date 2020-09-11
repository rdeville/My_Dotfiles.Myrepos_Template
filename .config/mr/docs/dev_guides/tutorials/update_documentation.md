# Mkdocs Tutorials

This repo which render the documentation is based on the tool [mkdocs][mkdocs].

Here is a little tutorial on how to add a page to the documentation.

## Setup your working environment

First thing to do once the repo is cloned is to setup your working environment.

To do so, please refer to the section [Setup myrepos
configuration][setup_myrepos].

## Work on the documentation

Second thing you need to know is you can work on the documentation and live see
your modification. To do so, once your working environment is ready, simply type
the following command :

```bash
# Assuming you are in ~/.config/mr
mkdocs serve
```

You will have an output similar to the following:

```bash
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  Documentation built in 0.27 seconds
[I 200602 10:31:44 server:296] Serving on http://127.0.0.1:8000
INFO    -  Serving on http://127.0.0.1:8000
[I 200602 10:31:44 handlers:62] Start watching changes
INFO    -  Start watching changes
[I 200602 10:31:44 handlers:64] Start detecting changes
INFO    -  Start detecting changes
```

Doing so, you will be able to access the documentation on
[http://localhost:8000](http://localhost:8000)

## Add a new page

By default, mkdocs generate the architecture of the documentation based on the
architecture of the documentation folder, the `~/.config/mr/docs` folder.

If you want to add new page, you will have two step to follow:

  - Add the page to the navigation in the mkdocs configuration file
  - Add the file to the architecture of the documentation

### Add the page to the mkdocs configuration file

First thing to do when adding your page is to add it to the `mkdocs.yml`
configuration file under the `nav` key.

For instance, let's assume you want to add a "chapter" called "User Guide" with
two page within, "Installation" and "Quick Start"

You will need to add the following content in the mkdocs.yml file:

```yaml
nav:
  - Home: index.md
  - User Guide:
    - Installation: user_guide/installation.md
    - Installation: user_guide/quick_start.md
```

### Add the file to the architecture of the documentation

Once this is done, you will need to add the file corresponding, otherwise you
will see following warnings:

```text
WARNING -  A relative path to 'user_guide/installation.md' is included in the 'nav' configuration, which is not found in the documentation files
WARNING -  A relative path to 'user_guide/quick_start.md' is included in the 'nav' configuration, which is not found in the documentation files
```

To do so, simply create the corresponding files:

```bash
touch user_guide/{installation.md,quick_start.md}
```

You can now write in this files the corresponding documentation with you
favorite test editor.

## Writing documentation

When writing your documentation, the theme used in this documentation will
generate a right sidebar with the table of content of the current page, as shown
in the image below:

![!Right Sidebar][mkdocs_material_right_sidebar]

This TOC sidebar is automatically generated based on the section depths of the
markdown file.

**REMARK** The top section of markdown title is not used in the TOC sidebar, it
is only used as a title of the page. For instance, assuming the following page
extract:

```markdown
# Title

## Section 1

Lorem Ipsum

## Section 2

### Subsection 2.1

Lorem Ipsum

### Subsection 2.2

Lorem Ipsum

```

The TOC sidebar generated will be:

```text
  Section 1
  Section 2
    Subsection 2.1
    Subsection 2.2
```

## References

For more information, please refer to:

  - [the mkdocs documentation][mkdocs]
  - [the mkdocs theme (mkdocs material) documentation][mkdocs_material]


[setup_myrepos]: ../../usage/setup_myrepos_configuration.md
[mkdocs_material_right_sidebar]: /assets/img/mkdocs_material_right_sidebar_toc.png
[mkdocs]: https://www.mkdocs.org/
[mkdocs_material]: https://squidfunk.github.io/mkdocs-material/getting-started/
