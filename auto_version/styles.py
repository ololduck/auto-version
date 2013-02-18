# -*- coding:utf-8 -*-

"""
auto_version.styles
~~~~~~~~~~~~~~~~~~~

auto_version.styles is the holder of all the different coding styles.

Each style is built on top of others, as they have multiple features in common. For instance, a Revision-based versionning has a feature used in <major>.<minor>.

I am still thinking about it.

.. todo::
    Implement more styles

"""
import re


class Revision:
    """
    Revision format is a simple, one-number versionning format: r<number>
    for example, r7 is the verison after r6.

    It is used in some DCVS, such as mercurial, or svn.
    """

    __format__ = r'\d+'

    def __init__(self, current_version):
        self.regex = re.compile(__format__)
        self.current_version = current_version

    def increment(self, level):
        """
        Performs the actual incrementation of the version number. The parameter ``level`` is ignored here, because there is only one.
        """
        version = self.current_version[1:]
        version = int(version)
        version = version + 1
        self.current_version = 'r%d' % version
        return self.current_version


class Doublet(Revision):
    """
    Double format is in the form <major>.<minor>

    It is pretty self-explainatory. Mostly used in very small projects, without a lot of dependencies.

    <major> begins most of the time at 0, indicating the in-development state of the project.

    Examples:
        * 0.5
        * 1.2
        * 1.53
    """

    __format__ = r'\d+\.\d+'

    def increment(self, level="minor"):
        """
        Performs increment of the version number, according to the given "level" parameter.
        Level may be one of the followings:

            * "minor" or 1: increments the <minor> part of version string
            * "major" or 0: increments the <major> part of version string, and resets <minor> to 0.
        """
        version = self.current_version.split('.')
        if(level == "minor" or level == 1):
            version[1] = version[1] + 1
        elif(level == "major" or level == 0):
            version[0] = version[0] + 1
            version[1] = 0
        else:
            raise ValueError("Invalid level of incrementation given.")
        return "%d.%d" % version


class Triplet(Revision):
    """
    Trpilet format is in the form <major>.<minor>.<patch>

    It is the most commonly used versionning 'style'.

    Examples:
        * 0.0.1
        * 1.0.2
    """

    __format__ = r'\d+\.\d+\.\d+'

    def increment(self, level="patch"):
        """
        Performs increment of version number, according to the given "level" parameter.

        Level may be one of the followings:

            * "patch" or 2: increments the <patch> part of the version string
            * "minor" or 1: increments the <minor> part of the version string, and resets <patch> to 0
            * "major" or 0: increments the <major> part of the version string, and resets <minor> and <patch> to 0
        """

        version = self.current_version.split('.')

        if(level == "patch" or level == 2):
            version[2] = version[2] + 1
        elif(level == "minor" or level == 1):
            version[1] = version[1] + 1
            version[2] = 0
        elif(level == "major" or level == 0):
            version[0] = version[0] + 1
            version[1] = 0
            version[2] = 0
        else:
            raise ValueError("Invalid level of incrementation given.")
        return "%d.%d.%d" % version

# class Full:
#     """
#     Full format, aka. :<major>.<minor>.<patch>+<status>-<build>
#     where <major>, <minor>, <patch> and <build> are numbers (aka, the actual version number. Well, except for the build number),
#     and <status> is one of the following:
#         * prealpha
#         * alpha
#         * beta
#         * rc
#         * release
#     """

#     FORMAT = r'\d+\.\d+\.\d+\+\w\-\d+'

#     def __init__(self):
#         pass

#     def increment(self, level):
#         pass

