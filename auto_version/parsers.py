"""
auto_version.parsers
~~~~~~~~~~~~~~~~~~~~

This module contains the main Parser class. This class is the one parsing the given files, and replacing the values by the new ones.
"""

import os
import re
from utils import import_style, detect_vcs, logger


class BasicParser:
    """
    This Class is a basic parser. It takes a list of files in argument, and the format of the versioning system, and performs the replacement.


    Expected instanciation arguments are:
        * files: an array of pathnames
        * current_version: a string containing the current version of the versionned project.
        * style: string to the auto_version.styles module class to use.
        * action *optionnal*: a string or number representing the action to perform.
    """

    def get_style_class_from_str(self, style):
        return import_style(style)

    def __init__(self, conf):
        self.conf = conf
        logger.debug("parser: self.conf=" + str(self.conf))
        if("files" in self.conf):
            if(type(self.conf["files"]) is list or type(self.conf["files"]) is tuple):
                for f in self.conf["files"]:
                    if(not os.path.exists(f)):
                        raise IOError("Could not access file %s. Please check path and/or your rights ont that file." % f)
                    elif(os.path.isdir(f)):
                        raise NotImplementedError("%s is a directory!" % f)
                self.conf["files"] = list(self.conf["files"])
            elif(type(self.conf["files"]) is str or type(self.conf["files"]) is unicode):
                f = self.conf["files"]
                if(os.path.isdir(f)):
                    raise NotImplementedError("%s is a directory!" % f)
                elif(not os.path.exists(f)):
                    raise IOError("Could not access file %s. Please check path and/or your rights ont that file." % f)
                self.conf["files"] = [f, ]
            else:
                raise RuntimeError("Could not determine type of given data")
        else:
            raise ValueError("You have not given any file to parse!")

        if("style" not in self.conf):
            raise ValueError("No style given")

        if("current_version" in self.conf):
            if(type(self.conf["current_version"]) is not str and type(self.conf["current_version"]) is not unicode):
                raise RuntimeError("current_version is not a string!")
        else:
            raise ValueError("Could not find current version. This may lead to serious things. I would personnaly prefere that you use a correct self.configuration file.")
            # TODO: Create a function search for the style pattern in the files.

    def perform(self):
        """
        Performs the actual value replacement, according to the given parameters.

        .. attention::

            This may be quite long on large files!
        """

        self.vcs = detect_vcs()()
        style = self.get_style_class_from_str(self.conf["style"])
        self.vcs.style = style
        logger.info(self.conf["current_version"])
        if(self.conf["current_version"] == ""):
            self.conf["current_version"] = self.vcs.get_current_version(with_status=True, increment=False)
            logger.info("vcs version = " + self.conf["current_version"])
        if(self.conf["action"] == "update"):
            if(self.vcs is not None):
                new_version = self.vcs.get_current_version(with_status=True)  # FIXME
            else:
                raise NotImplementedError("It seems you are trying to do some versioning sync with a non-supported versioning system (Are you really using one on this project?) Please feel free to send an issue at https://github.com/paulollivier/auto_versioning !")
        else:
            try:
                style_instance = style(self.conf["current_version"])
                new_version = style_instance.increment(self.conf["action"])
            except:
                logger.info("Style instance reported error trying to process version number. Trying with SCM info")
                new_version = self.vcs.get_current_version(with_status=False, increment=False)
                style_instance = style(new_version)
                new_version = style_instance.increment(self.conf["action"])
        logger.info("old version:" + self.conf["current_version"] + " new version: " + new_version)
        for f in self.conf["files"]:
            data = ""
            with open(f, 'r') as fd:
                data = fd.read()
            for m in re.finditer(self.conf["current_version"], data):
                data = data.replace(self.conf["current_version"], new_version)
            with open(f, 'w+') as fd:
                fd.write(data)
        if(self.vcs and self.conf["commit"] and self.conf["action"] != "update"):
            logger.info("setting new version %s to SCM" % new_version)
            self.vcs.set_version(files=self.conf["files"], version=new_version, prefix=self.conf["scm_prefix"])

        return new_version
