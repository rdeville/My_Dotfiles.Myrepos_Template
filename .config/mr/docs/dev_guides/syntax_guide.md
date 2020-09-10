# Syntax Guide

This file will describe code styles used in this repos to make code and
documentation more homogeneous.

## Versionning & Contribution

When developping and especially when commiting you work, try to make "beautiful"
commit, with a title and a description of what is done.

If your modification can be written in one line title (i.e. less than 50 char),
for instance, writing documentation in the README.md, avoid commit message like
"_Update README.md_", prefer "_Update section XXXX in README.md_" or even
better :

```text
Update section configuration in README.md

Add/Update section configuration which describe how to configure your prompt and
link to the related documentation.

```

Sometime you are not used to do this, you may not have time or you have a huge
commit which only do one thing (for instance, 30 update
files, which is only updating documentation).

Thus, above advice about commit are not mandatory, but **merge request MUST
follow the "beautiful" merge request guideline**. Merge request with only title
"merge `branch` on `master`" will need to be updated before being accepted.

Finally, when contributing, i.e. propose a merge request, ensure that your
personal configuration files are not versionned.

## Configuration Files

Configuation files related to development tools, such as `pyproject.toml`,
**MUST** have comment. If you add or update configuration files, please provide
comments above the variable to describe the use of variable and, if needed, why
you choose these values. This is especially true when deactivating testing tools
error or warnings.

## Python Files

Python files should respect PEP8. To ensure this, the CI use [flake8][flake8]
and [pylint][pylint].

To test PEP8 compliancy of python codes, you can go to `~/.config/mr`, install
python development requirements and run the tox command. Here is an example how
to do it:

```bash
# Go to ~/.config/mr
cd ~/.config/mr
# Assuming you do no use direnv and you do not create python virtual environment
python3 -m venv .virtual_env
# Activate the virtual environment
source .virtual_env/bin/activate
# Install python production and development dependencies
pip3 install -r requirements.txt
pip3 install -r requirements.dev.txt
# Finally, run the test process usin tox
tox
```

Moreover, here are some guidelines to follow to make python code  homogeneous:

  * When using `for` or `while` loop, prefer using variable starting with `i`
    followed by an explicit name than simply `i`, `j`, etc.<br>

    Even better, if you loop over an index use `idx` as prefix, and if you loop
    over items, use `i` as prefix.

    ??? Example "Example (Click to reveal)"
        ```python
        age_list=["10" "15" "17" "22" "35" "40"]
        # Loop over items
        for i_age in age_list:
        do
          print("You are " + i_age + "years old.")
        done
        # Loop over index
        for idx_age in len(age_list):
        do
          print("You are " + age_list[idx_age] + "years old.")
        done
        ```

  * When defining a method, please add [type hints][type_hint] describing expected types as
   method arguments and what is return by the method. Why ? Because the
   rendering of the documentation parse this type hints, for instance, see
   [main.py][main.py].

    ??? Example "Example (Click to reveal)"
        ```python
        def my_method(path:str, val_1: int, val_2: int) -> bool:
        ```


  * Docstring should follow [Google Python
   Styleguide][google_python_styleguide]. Why ? Because the rendring of this
   documentation parse docstring which are in this style, for instance, see
   [main.py][main.py].

    ??? Example "Example (Click to reveal)"
        ```python
        def save_sum(path:str, values: list) -> bool:
            """Compute some of integer in list and write result in file

            The method compute the sum of all integer passed as a list and save
            it in a specified file.

            Arguments:
              path: Path to the file where results will be stored
              values: List of integer that will be summed

            Return:
              Boolean to know if the save process in files worked or not.
            """
        ```

Using the two previous recommendation will result in the following
documentation using [mkdocstring][mkdocstring]:

??? example "Example of docstring rendered documentation (click to reveal)"
    === "Result"
        <div class="doc doc-object doc-function">
          <h2 class="doc doc-heading" id="main.save_sum">
          <code class="highlight language-python">
            save_sum<span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">values</span><span class="p">)</span>
          </code>
          <a class="headerlink" href="#main.save_sum" title="Permanent link"></a>
          </h2>
          <div class="doc doc-contents">
            <p>Compute some of integer in list and write result in file</p>
            <p>The method compute the sum of all integer passed as a list and save it in a specified file.</p>
            <p><strong>Parameters:</strong></p>
            <div class="md-typeset__scrollwrap">
              <div class="md-typeset__table">
                <table>
                  <thead>
                  <tr>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Description</th>
                    <th>Default</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr>
                    <td><code>path</code></td>
                    <td><code>str</code></td>
                    <td>
                      <p>Path to the file where results will be stored</p>
                    </td>
                    <td><em>required</em></td>
                  </tr>
                  <tr>
                    <td><code>values</code></td>
                    <td><code>list</code></td>
                    <td>
                      <p>List of integer that will be summed</p>
                    </td>
                    <td><em>required</em></td>
                  </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <p><strong>Returns:</strong></p>
            <div class="md-typeset__scrollwrap"><div class="md-typeset__table">
              <table>
                <thead>
                  <tr>
                    <th>Type</th>
                    <th>Description</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><code>bool</code></td>
                    <td>
                      <p>Boolean to know if the save process in files worked or not.</p>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
    === "Source Code"
        ```python
        def save_sum(path:str, values: list) -> bool:
            """Compute some of integer in list and write result in file

            The method compute the sum of all integer passed as a list and save
            it in a specified file.

            Arguments:
              path: Path to the file where results will be stored
              values: List of integer that will be summed

            Return:
              Boolean to know if the save process in files worked or not.
            """
            sum = 0
            for i_value in values:
              sum += i_value
            try:
              f= open(path,"w")
              f.write(sum)
              f.close()
            except:
              return false
        ```

## Bash Scripting

Bash script should follow some code styles which are describe below:

  * When using `function` or method, `for`, `while`, `case` or `if`, put respectively
    `{`, `do`, `do`, `esac` and `then` below the condition to test.<br>

    ??? Example "Example (Click to reveal)"
        ```bash
        functions name()
        {
          case $1 in
            [a-z]*)
              echo "Alphabet"
              ;;
            [0-9]*)
              if [[ $1 -lt 5 ]]
              then
                echo "Number less than 5"
              else
                echo "Number greater than 5"
              fi
              ;;
            *)
              echo "Unknown"
              ;;
          esac
        }
        ```

  * When using `for` or `while` loop, prefer using variable starting with `i`
    followed by an explicit name than simply `i`, `j`, etc.<br>

    ??? Example "Example (Click to reveal)"
        ```bash
        age_array("10" "15" "17" "22" "35" "40")
        for i_age in "${age_array[@]}"
        do
          echo "You are ${i_age} years old."
        done
        ```
    Even better, if you loop over an index use `idx` as prefix, and if you loop
    over items, use


  * Use 2 indentation **space** when defining a scope (method, loop, condition,
    etc.).

    ??? Example "Example (Click to reveal)"
        ```bash
        func()
        {
          people=("Alice" "Bob" "Carol" "David" "Eve")
          for i_people in "${people[@]}"
          do
            if [[ ${i_people} =~ a ]]
            then
              echo "${i_people}"
            else
              echo "I do not tell people name which does not have an 'a'"
            fi
          done
        }
        ```

  * When using "advanced" bashism, such as string substitution, write a comment
    above describing what you do in human readable format.

    For more informations about what I consider string substitution, see
    [tldp.org-String Manipulation][tldp_string_manipulaton], this is not
    mandatory but is here to help people not used to these syntax to understand
    what is done.

    ??? Example "Example (Click to reveal)"
        ```bash
        A="abcdabcda"
        # Replace 'cd' in ${A} by 'zy'
        B=${A/cd/zy}
        echo $B
        # Remove everything in before the last occurence of 'a'
        C=${A##*a}
        # Remove everything after the first occurence of c
        D=${A%%c*}
        ```

  * Document your method with a "docstring" like.

    ??? Example "Example (Click to reveal)"
        ```bash
        function func_name()
        {
          # This is a docstring like expliciting what func_name do
          # *PARAM $1: string, explicit description of the required (`*`) expected string
          # PARAM $2: string, explicit description of the optional expected string
          # NO PARAM: -> Means that NO PARAM is required or optional for this
          #             function
        }
        ```

  * Do not write more that 80 char lines of code, except when there is no other
    options or when using `echo`.

    ??? Question "Why ? (click to reveal)"
        Because I often have two or three code files open in splitted screen in
        vim, thus showing only 80 char per file.

  * All variable should be in lowercase execpt for configuration and constant
    variables that can be set in configuration files `host/` folder which are in
    uppercase. Prefer to use `_` between words in variable name. And when using
    variables, use `{}` around the variable usage.

    ??? Question "Why ? (click to reveal)"
        The lowercase is to make differences between constant/user defined
        variables and the computation variables.

        The `_` between word is to make variable name more human readable.

        The `{}` may add a heavy layout of reading but as I use lots of arrays
        and string manipulation, I now tends to use them all the time. Moreover
        this avoid issues like shown below:

        ```bash
        var="filename.sh"
        # When not using `{}`, line below will search for value of variable
        # `var_temp` instead of printing the value of ${var} + "_temp"
        echo "$var_temp"
        # While this line print ${var} + "_temp"
        echo "${var}_temp"
        ```

    ??? Example "Example (click to reveal)"

        ```bash
        git_username="Firstname Lastname"
        git_usermail="username@domain.tld"
        echo "${git_username} < ${git_usermail} >"
        ```

  - End your code files with a [vim modeline][vim_modeline].

    ??? Example "Example (click to reveal)"
        I usually tend to be explicit in my modeline:
        ```bash
        # ***********************************
        # EDITOR CONFIG
        # vim: ft=sh: ts=2: sw=2: sts=2
        # **********************************
        ```
        But a shorten modeline is valid too:
        ```bash
        # vim: ft=sh: ts=2: sw=2: sts=2
        ```
        This modeline tells to vim that

          * `ft=sh`: filetype is `sh`
          * `ts=2`: tabstop should be 2 space wide
          * `sw=2`: shiftwidth should be 2 space wide
          * `sts=2`: replace tab by a 2 space indent


!!! important
    As stated above, this code styles are not mandatory but here to provide
    guidelines. Moreover, I'm open to discussion to use other guidelines.

Below is an example using these code styles:

```bash
#!/bin/bash

# Description of the script. Which simply print the content of an array but
# replace value "item" of each cells by "toto-item" if item index is pair and
# "tata-item" if index is odd

method()
{
  # Print value of array but replace "item" by toto-item if item is pair and
  # tata-item if item is odd.
  # NO PARAM

  local my_array("item0" "item1" "item2" "item3")
  local idx_item=""

  for i_elem in "${my_array[@]}"
  do
    # Extract index of item that is at the end of the string
    idx_item=${i_elem##item}
    if [[ $(( idx_item % 2 )) -eq 0 ]]
    then
      # Replace item by toto-item
      echo "${i_elem/item/toto-item}"
    else
      # Replace item by tata-item
      echo "${i_elem/item/tata-item}"
    fi
  done
}

# *****************************************************************************
# EDITOR CONFIG
# vim: ft=sh: ts=2: sw=2: sts=2
# *****************************************************************************
```


## Markdown mkdocs flavor

When writing markdown documentation for mkdocs, please prefer following syntax:

  * For hyperlink, please use the following syntax:

    ```md
    [Text Content][ext_hyperlink_key]
    [Another Text Content][int_hyperlink_key]

    [ext_hyperlink_key]: https://external.link
    [int_hyperlink_key]: ../relative/path.md
    ```

  * For image, a lightbox plugin is installed. So to allow lightboxing of image
    in mkdocs documentation, please use the following syntax:

    ```md
    ![!Image Caption][image_key]

    [image_key]: ../relative/path/to/image.png
    ```

  * For the documentation, multiple markdown extension have been
    installed such as:

      * [Admonition][mkdocs_admonition_plugin]:

        Admonition is an extension
        included in the standard Markdown library that makes it possible to add
        block-styled side content to your documentation, e.g. summaries, notes,
        hints or warnings.

      * [Footnotes][mkdocs_footnotes_plugin]:

        Footnotes is another extension
        included in the standard Markdown library. As the name says, it adds the
        ability to add inline footnotes to your documentation.

      * [Metadata][mkdocs_metadata_plugin]:

        Metadata is an extension included in
        the standard Markdown library that makes it possible to control certain
        properties in a page-specific context, e.g. the page title or
        description.

      * [Permalinks][mkdocs_permalink_plugin]:

        Permalinks are a feature of the
        Table of Contents extension, which is part of the standard Markdown
        library.

      * [PyMdown][mkdocs_pymdown_plugin]:

        PyMdown Extensions is a collection of
        Markdown extensions that add some great missing features to the standard
        Markdown library.

      * [Mermaid][mkdocs_mermaid_plugin]:

        Mermaid is a tool that generates
        diagrams and charts, from markdown-inspired text definitions

Allowing you to enrich the content of the documentation.

[mkdocs_admonition_plugin]: https://squidfunk.github.io/mkdocs-material/extensions/admonition/
[mkdocs_codehilite_plugin]: https://squidfunk.github.io/mkdocs-material/extensions/codehilite/
[mkdocs_footnotes_plugin]: https://squidfunk.github.io/mkdocs-material/extensions/footnotes/
[mkdocs_metadata_plugin]: https://squidfunk.github.io/mkdocs-material/extensions/metadata/
[mkdocs_permalink_plugin]: https://squidfunk.github.io/mkdocs-material/extensions/permalinks/
[mkdocs_pymdown_plugin]: https://squidfunk.github.io/mkdocs-material/extensions/pymdown/
[mkdocs_mermaid_plugin]: https://mermaid-js.github.io/mermaid/#/flowchart

[flake8]: https://flake8.pycqa.org/en/latest/
[pylint]: https://pylint.org/
[google_python_styleguide]: https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings
[tldp_string_manipulaton]: https://www.tldp.org/LDP/abs/html/string-manipulation.html
[vim_modeline]: https://vim.fandom.com/wiki/Modeline_magic
[main.py]: references/main.py.md
[type_hint]: https://docs.python.org/3/library/typing.html
[mkdocstring]: https://pawamoy.github.io/mkdocstrings/
