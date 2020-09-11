# FAQ & Known issues

## FAQ

### Troubleshoot


??? error "`Direnv` tell me that `.envrc` file is blocked (click to reveal)"

    When downloading repo with a file `.envrc` or when creating a file `.envrc`
    in a folder, `direnv` may print the following line:

    ```text
    direnv: error PATH/TO/.envrc is blocked. Run `direnv allow` to approve its content
    ```

    This is normal as `direnv` come with a protection mecanism to not run
    `.envrc` files which are not explicitly allowed. Indeed, for instance, if a
    malicious person write the command `rm -rf ${HOME}` in the `.envrc` and if
    this file would have been automatically run, this will lead to disastrous
    events (in this example, you will lose every files and folder in your
    `HOME`)

    In this case, check the content of the file provided in the error. If you
    agree with it content you can allow it for direnv with the following command
    `direnv allow`.

    If you modify the file `.envrc` once already allowed, this file will
    automatically be denied by `direnv` as its hash differs from the previous
    version. So after a modification on an already allowed `.envrc` you will
    need to allow this new version.

??? error "`Direnv` taking a long time to initialize (click to reveal)"

    Sometimes, if your script `activate_direnv` do a lots of things (or
    especially when activating the directory environment for the first time),
    you might see the following line:

    ```bash
    direnv: ([/usr/bin/direnv export bash]) is taking a while to execute. Use CTRL-C to give up.
    ```

    There are two possibilities:

      - Either your script `activate_direnv` is long to be processed. In this
        case, there is nothing much you can do except optimizing your script.

      - Either there is a bug in your script `activate_direnv`. The best thing
        to do is to temporarly deactivate `direnv` automatic behaviour. This can
        easily be done by moving your file `.envrc` at the root of the repo.
        Then execute manually the script `activate_direnv` to find its bugs.


??? error "`Direnv` tell me it can not export `PS1`"

    In the provided `activate_direnv` script, we automatically load the python
    directory environment. Normally, doing this should update variable `PS1`
    which is used to display information in before each command (see [Prompt
    Customization][prompt_customization]).

    Default for `bash` is usually of the form `$(username)@$(hostname)`, as
    shown below:

    ```bash
    username@hostname:~ >
    ```

    Well, direnv is unable to update the `PS1` variable and will print the
    following error:

    ```text
    direnv: PS1 cannot be exported. For more information see https://github.com/direnv/direnv/wiki/PS1
    ```

    Do not worry, this will not make direnv not working, it just means that when
    your python virtual environment will be loaded, this virtual environment
    will not be shown as usual, like shown below:

    ```bash
    (python_venv)username@hostname:~ >
    ```

    For more information, see: https://github.com/direnv/direnv/wiki/PS1


[prompt_customization]: https://wiki.archlinux.org/index.php/Bash/Prompt_customization#Prompts
