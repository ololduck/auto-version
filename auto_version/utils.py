"""
auto_version.utils
~~~~~~~~~~~~~~~~~~

Contains some utilities used in the project. You should not have to bother with it.
"""

import os
import json


class ConfManager:
    """
    Configuration manager. It makes the bridge and the intelligence between the cli args and the configuration file, who may be present. Or not. Whatever.

    .. todo:

        assure the configuration integrity. Some preliminar cli args are parsed and checked for availability by the argparse module, but not all of them! Think to raise an exception if the "files" attribute is not present anywhere, for instance.
    """

    conf = {}

    def __init__(self, cli_args):
        self.cli_args = cli_args
        self.file_conf = None

        if(os.path.exists(self.cli_args["conf"])):
            with open(self.cli_args["conf"], 'r') as f:
                self.file_conf = json.loads(f.read())
        self.conf = self.file_conf
        self.conf.update(self.cli_args)

    def get_conf(self):
        """
        return the current state of the configuration dictionnary
        """
        return self.conf

    def save_conf(self, d):
        """
        Saves the configuration to file.
        The configuration is updated with the given dictionnary.

        .. warning::

            given keys are overwritten!
        """
        self.conf.update(d)
        with open(self.cli_args["conf"], "w+") as f:
            f.write(json.dumps(self.file_conf, sort_keys=True, indent=4, separators=(',', ': ')))
