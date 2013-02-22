"""
auto_version.parsers
~~~~~~~~~~~~~~~~~~~~

This module contains the main Parser class. This class is the one parsing the given files, and replacing the values by the new ones.
"""

import os
import re
from auto_version.utils import import_style, detect_vcs


class BasicParser:
    """
    This Class is a basic parser. It takes a list of files in argument, and the format of the versionning system, and performs the replacement.


    Expected instanciation arguments are:
        * files: an array of pathnames
        * current_version: a string containing the current version of the versionned project.
        * style: string to the auto_version.styles module class to use.
        * action *optionnal*: a string or number representing the action to perform.
    """

    files = []
    current_version = ""
    action = None

    def get_style_class_from_str(self, style):
        return import_style(style)

    def __init__(self, **kwargs):
        if("files" in kwargs):
            if(type(kwargs["files"]) is list or type(kwargs["files"]) is tuple):
                for f in kwargs["files"]:
                    if(not os.path.exists(f)):
                        raise IOError("Could not access file %s. Please check path and/or your rights ont that file." % f)
                    elif(os.path.isdir(f)):
                        raise NotImplementedError("%s is a directory!" % f)
                self.files = list(kwargs["files"])
            elif(type(kwargs["files"]) is str or type(kwargs["files"]) is unicode):
                f = kwargs["files"]
                if(os.path.isdir(f)):
                    raise NotImplementedError("%s is a directory!" % f)
                elif(not os.path.exists(f)):
                    raise IOError("Could not access file %s. Please check path and/or your rights ont that file." % f)
                self.files = [f, ]
            else:
                raise RuntimeError("Could not determine type of given data")
        else:
            raise ValueError("You have not given any file to parse!")

        if("style" in kwargs):
            self.style = kwargs["style"]
        else:
            raise ValueError("No style given")

        if("current_version" in kwargs):
            if(type(kwargs["current_version"]) is not str and type(kwargs["current_version"]) is not unicode):
                raise RuntimeError("current_version is not a string!")
            self.current_version = kwargs["current_version"]
        else:
            raise ValueError("Could not find current verion. This may lead to serious things. I would personnaly prefere that you use a correct configuration file.")
            # TODO: Create a function search for the style pattern in the files.

        if("action" in kwargs):
            self.action = kwargs["action"]

    def perform(self):
        """
        Performs the actual value replacement, according to the given parameters.

        .. attention::

            This implementation may be quite long on large files!
        """

        style = self.get_style_class_from_str(self.style)(self.current_version)

        new_version = style.increment(self.action)
        self.vcs = detect_vcs()(style)
        for f in self.files:
            data = ""
            with open(f, 'r') as fd:
                data = fd.read()
            for m in re.finditer(self.current_version, data):
                data = data.replace(self.current_version, new_version)
            with open(f, 'w+') as fd:
                fd.write(data)

        self.vcs.set_version(new_version)

        return new_version
