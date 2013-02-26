"""
auto_version.dvcs
~~~~~~~~~~~~~~~~~

This modules contains all the implementation for versionning system automation.

see `Issue#1 <https://github.com/paulollivier/auto_versionning/issues/1>`_

The resulting version number will be in the form `<ChosenStyle>+<VCSStyle>`.

For git, VCSStyle is in the form `pre<number_of_commits_since_last_tag>-<sha_hash_of_last_commit>-<is_dirty?>`

If the user wants to use DVCS system, the option --use-vcs should be present, or "use_vcs": True should be present in config. This way, people won't find creepy hashes in their version string.
"""

import os
from subprocess import check_output, check_call


class BaseVCS:
    """
    Base VCS class

    .. attention::

        Do not use, use the actual vcs implementations instead
    """

    __meta_dir__ = ".meta"  # Should be overriden to reflect the meta-information folder for each system.

    def __init__(self):
        self.meta_info_present = self.__meta_dir__ in os.listdir(os.path.abspath('.'))

    def purify_raw_version(self, version):
        """
        trims unused chars for version parsing.

        e.g. v1.0.1 becomes 1.0.1

        :param: version: a string representing the raw version got by the VCS.

        :return: a string containing only the version string
        """
        pass

    def get_status(self):
        """
        Returns the `status` of the repository
        """
        raise NotImplementedError("This versionning class is not designed to be used, but rather as a base for actual implementations to rely on.")

    def get_current_version(self, with_status=False):
        """
        Return the current version, from the state of the repository.
        """
        raise NotImplementedError("This versionning class is not designed to be used, but rather as a base for actual implementations to rely on.")

    def set_version(self, version=None):
        """
        When a verison increment is made, update the vcs
        """
        raise NotImplementedError("This versionning class is not designed to be used, but rather as a base for actual implementations to rely on.")


class Git(BaseVCS):
    """
    Provides git support, via git tags. As many tag their commits with release numbers, it is a good idea to sync auto-version with these tags.
    """

    __meta_dir__ = ".git"

    def __init__(self):
        self.status = None
        BaseVCS.__init__(self)

    def _update_index(self):
        """
        Updates the git index.
        """
        check_call(["git", "update-index", "--refresh", "-q"])

    def _get_describe(self, increment=True):
        if(not self.status):
            s = check_output(["git", "describe", "--tags", "--dirty"])  # TODO: actually, we force users to use vX.X(...) tags. find an other way. This is a bit unsafe.
            print(type(s), s)
            self.status = [str(s) for s in s.strip('\n').split('-')]  # check_output returns bytes
            print("self.status = " + str(self.status))
            if(len(self.status) > 1 and increment):
                print(self.status[0])
                self.status[0] = self.style(self.status[0][1:]).increment()

        return self.status

    def get_status(self):
        self._update_index()
        if(self.status is None):
            print(self._get_describe())
        print("self.status fait %d de long" % len(self.status))
        if(len(self.status) == 4):
            print(self.status[1:])
            return 'pre%s-%s-%s' % self.status[1:]
        elif(len(self.status) == 3):
            print(self.status[1:])
            return "pre%s-%s" % (self.status[1], self.status[2])
        else:
            return ""

    def get_current_version(self, with_status=False, increment=True):
        self._update_index()
        print(self._get_describe(increment=increment))
        if(with_status):
            print("".join((self.status[0][1:], self.get_status())))
            return "".join((self.status[0][1:], self.get_status()))
        return self.status[0]

    def set_version(self, version=None):
        if(version is not None):
            check_call(["git", "tag", version])
