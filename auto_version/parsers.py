"""
auto_version.parsers
~~~~~~~~~~~~~~~~~~~~

This module contains the main Parser class. This class is the one parsing the given files, and replacing the values by the new ones.
"""

import os

class BasicParser:
    """
    This Class is a basic parser. It takes a list of files in argument, and the format of the versionning system, and performs the replacement.


    Expected instanciation arguments are:
        * files: an array of pathnames
        * current_version: a string containing the current version of the versionned project.
        * style: reference to any non-instanciated member of the auto_version.styles module.
        * action *optionnal*: a string or number representing the action to perform.
    """

    files = []
    current_version = ""
    action = None


    def __init__(self, **kwargs):
        if("files" in kwargs):
            if(type(kwargs["files"]) is list or type(kwargs["files"]) is tuple):
                for f in kwargs["files"]:
                    if(not os.path.exists(f)):
                        raise IOError("Could not access file %s. Please check path and/or your rights ont that file." % f)
                    elif(os.path.is_dir(f)):
                        raise NotImplementedError("%s is a directory!" % f)
                self.files = list(kwargs["files"])
            elif(type(kwargs["files"]) is str):
                f = kwargs["files"]
                if(not os.path.exists(f)):
                    raise IOError("Could not access file %s. Please check path and/or your rights ont that file." % f)
                elif(os.path.is_dir(f)):
                    raise NotImplementedError("%s is a directory!" % f)
                self.files = [f,]
            else:
                raise RuntimeError("Could not determine type of given data")
        else:
            raise ValueError("You have not given any file to parse!")

        if("style" in kwargs):
            if("increment" not in kwargs["style"].__dict__):
                raise ValueError("Given style to use has no increment method")
            self.style = kwargs["style"]
        else:
            raise ValueError("No style given")

        if("current_version" in kwargs):
            if(type(kwargs["current_version"]) is not str):
                raise RuntimeError("current_version is not a string!")
            self.current_version = kwargs["current_version"]
        else:
            print("No current version given. I will search for it now, but it may be long, and may be incorrect.")
            # TODO: Create a function search for the style pattern in the files.

        if("action" in kwargs):
            self.action = kwargs["action"]

    def perform(self):
        """
        Performs the actual value replacement, according to the given parameters.

        .. attention::

            This implementation may be quite long on large files!
        """
        s = __import__(self.style)
        style = s(self.current_version)
        new_version = style.increment(self.action)
        for f in self.files:
            data = ""
            with open(f, 'r') as fd:
                data = fd.read()
            match = data.findall(self.current_version)
            for m in match:
                data = data.replace(self.current_version, new_version)
            with open(f, 'w+') as fd:
                fd.write(data)




