# -*- coding:utf-8 -*-

"""
auto_version.styles
~~~~~~~~~~~~~~~~~~~

auto_version.styles is the holder of all the different coding styles.

Each style is built on top of others, as they have multiple features in common. For instance, a Revision-based versioning has a feature used in <major>.<minor>.

I am still thinking about it.

.. todo::
    Implement more styles

"""
import re
from auto_version.utils import logger


class BaseStyle:
    """
    This is the base style every Style class should inherit from.
    """

    def __init__(self, current_version):
        logger.debug("style = " + str(current_version))
        self.regex = re.compile(self.__format__)
        self.current_version = current_version
        if(self.regex.match(self.current_version) is None):
            raise ValueError("The current version you provided does not correspond to the chosen version style. Please review your configuration file and/or your cli args.")

    @staticmethod
    def get_pure_version_string(style_class, string):
        """
        Returns only the part matching the version string, so we can isolate it in a string
        """
        match = re.search(style_class.__format__, string)
        if(match):
            return string[match.start():match.end()]
        return None


class Revision(BaseStyle):
    """
    Revision format is a simple, one-number versioning format: r<number>
    for example, r7 is the version after r6.

    It is used in some DCVS, such as mercurial, or svn.
    """

    __format__ = 'r\d+'

    def increment(self, level=None):
        """
        Performs the actual incrementation of the version number. The parameter ``level`` is ignored here, because there is only one.
        """
        version = self.current_version[1:]
        version = int(version)
        version = version + 1
        return 'r%d' % version


class Doublet(BaseStyle):
    """
    Double format is in the form <major>.<minor>

    It is pretty self-explainatory. Mostly used in very small projects, without a lot of dependencies.

    <major> begins most of the time at 0, indicating the in-development state of the project.

    Examples:
        * 0.5
        * 1.2
        * 1.53
    """

    __format__ = '\d+\.\d+'

    def increment(self, level="minor"):
        """
        Performs increment of the version number, according to the given "level" parameter.
        Level may be one of the followings:

            * "minor" or 1: increments the <minor> part of version string
            * "major" or 0: increments the <major> part of version string, and resets <minor> to 0.
        """
        version = [int(n) for n in self.current_version.split('.')]
        if(level == "minor" or level == 1):
            version[1] = int(version[1]) + 1
        elif(level == "major" or level == 0):
            version[0] = int(version[0]) + 1
            version[1] = 0
        else:
            raise ValueError("Invalid level of incrementation given.")
        return "%d.%d" % (version[0], version[1])


class Triplet(BaseStyle):
    """
    Trpilet format is in the form <major>.<minor>.<patch>

    It is the most commonly used versioning 'style'.

    Examples:
        * 0.0.1
        * 1.0.2
    """

    __format__ = '\d+\.\d+\.\d+'

    def increment(self, level="patch"):
        """
        Performs increment of version number, according to the given "level" parameter.

        Level may be one of the followings:

            * "patch" or 2: increments the <patch> part of the version string
            * "minor" or 1: increments the <minor> part of the version string, and resets <patch> to 0
            * "major" or 0: increments the <major> part of the version string, and resets <minor> and <patch> to 0
        """

        version = [int(n) for n in self.current_version.split('.')]

        if(level == "patch" or level == 2):
            version[2] = int(version[2]) + 1
        elif(level == "minor" or level == 1):
            version[1] = int(version[1]) + 1
            version[2] = 0
        elif(level == "major" or level == 0):
            version[0] = int(version[0]) + 1
            version[1] = 0
            version[2] = 0
        else:
            raise ValueError("Invalid level of incrementation given.")
        return "%d.%d.%d" % (version[0], version[1], version[2])


class Full(BaseStyle):
    """
    Full format, aka. :<major>.<minor>.<patch>+<status>-<build>
    where <major>, <minor>, <patch> and <build> are numbers (aka, the actual version number. Well, except for the build number),
    and <status> is one of the following:

        * prealpha
        * alpha
        * beta
        * rc
        * release

    .. warning::

        NOT YET IMPLEMENTED!
    """

    __format__ = '\d+\.\d+\.\d+\+\w\-\d+'

    def __init__(self):
        raise NotImplementedError()

    def increment(self, level="build"):
        raise NotImplementedError()
