============
auto-version
============

+---------+-------------------------------------------------------------------------------+
| master  | .. image:: https://travis-ci.org/paulollivier/auto-version.png?branch=master  |
+---------+-------------------------------------------------------------------------------+
| develop | .. image:: https://travis-ci.org/paulollivier/auto-version.png?branch=develop |
+---------+-------------------------------------------------------------------------------+

This project consists of a small utility to perform semi-automatic
version number increase.

It is designed for use with a version control system like `git <http://git-scm.org>`_.

Documentation is available at `ReadTheDocs <https://auto-version.readthedocs.org/>`_. If you want the lastest stable release, please look at the ``latest`` documentation. If you want to get information about the latest features, please look at the ``develop`` documentation. For now, I recommand to read the ``develop`` branch.

Contributing
------------

Please feel free to contribute.

If you have a versioning style you would like to be merged in the main repository, and distributed via PyPI, send a pull request.

DISCLAIMER
----------

.. warning::

    This is ALPHA software. Do not use on critical environments, as it is not safe at all for now. For instance, it may alter any other string matching the current version umber when running the version increment. This is not really likely to happen, but it must be known. A way to fix this problem is being thought.

    PLEASE READ THE DOCUMENTATION BEFORE ANY USE
