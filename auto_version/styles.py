# -*- coding:utf-8 -*-

"""
auto_version.styles is the holder of all the different coding styles.

.. todo::
    Implement more styles

"""
import re


class Full:
    """
    Full format, aka. :<major>.<minor>.<patch>+<status>-<build>
    where <major>, <minor>, <patch> and <build> are numbers (aka, the actual version number. Well, except for the build number),
    and <status> is one of the following:
        * prealpha
        * alpha
        * beta
        * rc
        * release
    """

    FORMAT = r'\d+\.\d+\.\d+\+\w\-\d+'

    def __init__(self):
        pass

    def increment(self, level):
        pass

