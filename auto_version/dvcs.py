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
    """

    __meta_dir__ = ".meta"  # Should be overriden to reflect the meta-information folder for each system.

    def __init__(self):
        self.meta_info_present = self.__meta_dir__ in  os.listdir(os.path.abspath('.'))

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

class Git(BaseVCS):
    """
    Provides git support, via git tags. As many tag their commits with release numbers, it is a good idea to sync auto-version with these tags.
    """

    __meta_dir__ = ".git"

    def __init__(self):
        self.status = None
        super(BaseVCS, self).__init__()

    def _update_index(self):
        """
        Updates the git index.
        """
        check_call(["git", "update-index", "--refresh"])

    def _get_describe(self):
        if(not self.status):
            self.status = check_output(["git", "describe", "--tags", "--dirty"])  # TODO: actually, we force users to use vX.X(...) tags. find an other way. This is a bit unsafe.
        return self.status

    def get_status(self):
        self._update_index()
        self._get_describe()
        try:
            s = [str(s) for s in self.status.strip('\n').split('-')]
            return 'pre%s-%s-%s' % s[1:]
        except:
            s = [str(s) for s in self.status.strip('\n').split('-')]
            return 'pre%s-%s' % s[1:]

    def get_current_version(self, with_status=False):
        self._update_index()
        self._get_describe()
        s = [str(s) for s in self.status.strip('\n').split('-')]
        if(with_status):
            return "".join(s[0][1:], self.get_status())

