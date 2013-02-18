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

    The conf variable is a dictionnary, loaded from a json file.

    .. todo:

        assure the configuration integrity. Some preliminar cli args are parsed and checked for availability by the argparse module, but not all of them! Think to raise an exception if the "files" attribute is not present anywhere, for instance.
    """

    conf = {}

    def __init__(self, cli_args):
        self.cli_args = cli_args
        if(self.cli_args["files"] is None):
            del self.cli_args["files"]
        self.file_conf = None

        if(os.path.exists(self.cli_args["conf"])):
            if(self.cli_args["verbosity"] >= 2):
                print("Found config file %s" % self.cli_args["conf"])
            with open(self.cli_args["conf"], 'r') as f:
                data = f.read()
                if(self.cli_args["verbosity"] >= 2):
                    print(data)
                self.file_conf = json.loads(data)
            self.conf = self.file_conf
        self.conf.update(self.cli_args)
        if("files" in self.conf):
            if(self.conf["verbosity"] >= 3):
                print(self.conf["files"], type(self.conf["files"]))
            if(type(self.conf["files"]) is not list and
                type(self.conf["files"]) is not tuple and
                type(self.conf["files"]) is not str and
                type(self.conf["files"]) is not unicode):
                raise ValueError("Could not find the files to parse anywhere!")
        else:
            if(self.conf["verbosity"] >= 2):
                print("No key \"files\" in conf!")
            raise ValueError("Could not find the files to parse anywhere!")

        if("current_version" not in self.conf):
            raise ValueError("Could not find current verion. This may lead to serious things. I would personnaly prefere that you use a correct configuration file.")
        if("action" not in self.conf):
            raise ValueError("no action given! nothing to do \\o/")

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
