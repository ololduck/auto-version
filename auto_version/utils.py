"""
auto_version.utils
~~~~~~~~~~~~~~~~~~

Contains some utilities used in the project. You should not have to bother with it.
"""

import os
import json
import logging

logger = logging.getLogger("auto_version")
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


import styles
import dvcs


def import_style(name):
    """
    Simple utility function, taken from the __import__ docstring to import classes.
    """
    mod = __import__('auto_version.styles', fromlist=[name])
    klass = getattr(mod, name)
    return klass


def detect_vcs():
    """
    Detects the versioning system in use.

    .. attention::

        it does not currently handle multi-vcs systems

    .. todo::

        find a way to make this function auto-updating according to the classes loaded

    """
    dir_list = os.listdir(os.path.abspath('.'))
    klass = None
    for el in dir_list:
        if(el == ".git"):
            klass = dvcs.Git
            break
    return klass


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
        if(self.cli_args["current_version"] is None):
            del self.cli_args["current_version"]
        self.file_conf = None

        if(os.path.exists(self.cli_args["conf"])):
            logger.info("Found config file %s" % self.cli_args["conf"])
            with open(self.cli_args["conf"], 'r') as f:
                data = f.read()
                logger.debug(data)
                self.file_conf = json.loads(data)
            self.conf = self.file_conf
        if(self.cli_args["current_version"] == ""):
            del self.cli_args["current_version"]
        logger.debug("cli_args: " + str(self.cli_args))
        self.conf.update(self.cli_args)
        if("files" in self.conf):
            logger.info(self.conf["files"] + " " + str(type(self.conf["files"])))
            if(type(self.conf["files"]) is not list and
                type(self.conf["files"]) is not tuple and
                type(self.conf["files"]) is not str and
                type(self.conf["files"]) is not unicode):
                raise ValueError("Could not find the files to parse anywhere!")
        else:
            logger.error("No key \"files\" in conf!")
            raise ValueError("Could not find the files to parse anywhere!")

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
