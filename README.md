# auto_versionning

This project consists of a small utility to perform semi-automatic version number increase.

It is designed for use with a versionning system, supporting event hooks, like [git](http://git-scm.org)

## installation

First of all, you must get the code:

    git clone git@github.com:paulollivier/auto_versionning.git
    cd auto_versionning

Next, you want to add the main `pyrelease.py` executable to you `PATH`.

If you are on *nix, you can copy the file to a `PATH`-enabled directory. I like to use `~/bin`.

    cp pyrelease.py ~/bin/pyrelease

You're done.

## Usage

main usage:

    pyrelease COMMAND

First time:
You have to generate a config file for your project. So `cd` to your project directory, and run `pyrelease`. You should now notice a `pyrelease.conf` file.

It is a simple text file, with JSON-style information:

    {
    "files": [
        {
          "path": "put on file path here",
          "pattern": "\\d+\\.\\d+\\.\\d+\\-\\d+"
        },
        {
          "path": "put another file path here",
          "pattern": "\\d+\\.\\d+\\.\\d+\\-\\d+"
        }
      ]
    }

The file content may need some precision.

* `"files"`: This is the most important part of the configuration file.
    It contains multiple entries on all the files pyrelease must watch.

    * `path`: the path to the watched file.
    * `pattern`: this is the regex style pattern to the version string in your file.
        examples:

        * `\\d+\\.\\d+\\.\\d+\\-\\d+` : matches <major>.<minor>.<patch>-<build>
        * `\\d+\\.\\d+\\.\\d+`: matches <major>.<minor>.<patch>
        Other formatting are not currently accepted.

Some other options will be added when you run the program, but you shouldn't have to worry about it.

Now that you configured your project, you may use any of the commands:
* build
* patch
* minor
* major

You're done.
