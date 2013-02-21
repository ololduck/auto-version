================
auto_versionning
================

+---------+-----------------------------------------------------------------------------------+
| master  | .. image:: https://travis-ci.org/paulollivier/auto_versionning.png?branch=master  |
+---------+-----------------------------------------------------------------------------------+
| develop | .. image:: https://travis-ci.org/paulollivier/auto_versionning.png?branch=develop |
+---------+-----------------------------------------------------------------------------------+

This project consists of a small utility to perform semi-automatic
version number increase.

It is designed for use with a versionning system, supporting event
hooks, like `git <http://git-scm.org>`_

Documentation is available at `ReadTheDocs <https://auto-version.readthedocs.org/>`_

Contributing
------------

Please feel free to contribute.

If you have a versionning style you would like to be merged in the main repository, and distributed via PyPI, send a pull request.

DISCLAIMER
----------

This is beta software. Do not use on critical environments, as it is not totaly safe for now. For instance, it may alter any other string matching the current version umber when running the version increment. This is not really likely to happen, but it must be known. A way to fix this problem is being thought.
