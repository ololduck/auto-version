#!/usr/bin/env python

__version__ = "0.1.3"

import argparse
import logging

from auto_version.utils import ConfManager, logger
from auto_version.parsers import BasicParser

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', default=None, help="The action to perform, eg. increment 'build', 'patch', 'rev' ... Please see documentation for full list")
    parser.add_argument('--files', '-f', nargs="+", help="the file[s] to check for version string[s]")
    parser.add_argument('--conf', default="version.conf", help="the configuration file to use")
    parser.add_argument('--current_version', "-cv", default="", help="The version string to use. WARNING: overrides the one provided in configuration file!")
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)

    args = vars(parser.parse_args())

    loglvl = args["verbosity"]
    if(loglvl == 0):
        logger.setLevel(logging.ERROR)
    elif(loglvl == 1):
        logger.setLevel(logging.WARNING)
    elif(loglvl == 2):
        logger.setLevel(logging.INFO)
    elif(loglvl >= 3):
        logger.setLevel(logging.DEBUG)

    try:
        logger.info("Starting auto_versionning v" + __version__)
        cf = ConfManager(args)
        conf = cf.get_conf()
        logger.debug(str(conf))
        if("scm_prefix" in conf):
            p = BasicParser(files=conf["files"], style=conf["style"], action=conf["action"], current_version=conf["current_version"], scm_prefix=conf["scm_prefix"])
        else:
            p = BasicParser(files=conf["files"], style=conf["style"], action=conf["action"], current_version=conf["current_version"])
        conf["current_version"] = p.perform()
        del conf["verbosity"]
        del conf["action"]
        del conf["conf"]
        cf.save_conf(conf)
    except:
        logger.exception("Something went wrong! Please report the following info, go to https///github.com/paulollivier/auto_versionning, and fill in an issue.")
