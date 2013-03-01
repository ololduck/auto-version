.. auto-version documentation master file, created by
   sphinx-quickstart on Mon Feb 18 14:35:23 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

auto-version's documentation
============================

.. warning::

    THIS IS ALPHA GRADE SOFTWARE. PLEASE READ CAREFULLY THE PRESENT DOCUMENTATION

.. toctree::

.. contents:: Table of Contents
   :depth: 3

Installation
------------

Just run

::

    pip install auto-version

Usage
-----

Manual and semi-manual
~~~~~~~~~~~~~~~~~~~~~~

You may use it entirely from the CLI, but it may not be advised for projects. The cli is just htere for convenience.

It is intended to be used via a configuration file, by default named *version.conf*

Here is the one used for this module:

.. code:: json

    {
        "files": "auto_version/main.py",
        "current_version": "0.1.0",
        "style": "Triplet"
    }

The ``style`` option is a string representing the name of the style class to use. Here, I use the Triplet format, which consists in ``<major>.<minor>.<patch>``.

``"files"`` may be a simple string, or an array, like this:

.. code:: json

    {
        "files": [
            "path/to/file",
            "other/path/to/file"
        ],
        other stuff,
        blablabla
    }

See `auto_version.styles`_ for more available version string styles.

VCS Integration
~~~~~~~~~~~~~~~

.. warning::

    This is still a rather unstable feature, your workflow may be changed, and possibly destroyed.

If versioning system is detected (via the presence or not of a distinctive versioning directory, like ``.git``), ``auto-version`` uses the informations present in the SCM to determine the version numbers. For git, it is via the ``git tag`` and ``git describe`` commands;

This still requires a ``version.conf`` file, but only three parameters are used::

    {
        "files": "file_to_manage",
        "style": "Triplet",
        "scm_prefix": "prefix to use for version tagging"
    }

Sample Usage
++++++++++++

.. code:: bash

    $ cd /tmp
    $ git init testing
    $ cd testing
    $ echo "0.0.1" > hello.txt
    $ echo '{ "files": "hello.txt", "style": "Triplet, "scm_prefix": ""}' > version.conf
    $ git add hello.txt version.conf
    $ git commit -m "Initial commit"
    $ git tag 0.0.1
    $ auto-version update
    $ cat hello.txt
    0.0.1
    $ echo "hi\!" >> hello.txt
    $ git add hello.txt
    $ git commit -m "Modified hello.txt to better reflect my understanding of the world, from a programmer\'s perspective"
    $ auto-version update
    $ cat hello.txt
    0.0.2-pre1-0bf45de
    hi!
    $ auto-version patch
    $ cat hello.txt
    0.0.2
    hi!






In-depth documentation for trve l33t hackerz of the internets
-------------------------------------------------------------

Organisation
~~~~~~~~~~~~

.. include:: organisation.rst

Modules detail
~~~~~~~~~~~~~~
.. automodule:: auto_version.styles
   :members:

.. automodule:: auto_version.dvcs
   :members:

.. automodule:: auto_version.parsers
   :members:




Less usefull stuff
~~~~~~~~~~~~~~~~~~

.. automodule:: auto_version.utils
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

