#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1.0"

import argparse

from auto_version.utils import ConfManager
from auto_version.parsers import BasicParser

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', default=None, help="The action to perform, eg. increment 'build', 'patch', 'rev' ... Please see documentation for full list")
    parser.add_argument('--files', '-f', nargs="+", help="the file[s] to check for version string[s]")
    parser.add_argument('--conf', default="version.conf", help="the configuration file to use")
    parser.add_argument('--curr_version', "-cv", default=None, help="The version string to use. WARNING: overrides the one provided in configuration file!")
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)

    args = vars(parser.parse_args())

    cf = ConfManager(args)
    conf = cf.get_conf()
    p = BasicParser(files=conf["files"], style=conf["style"], action=conf["action"], current_version=conf["current_version"])
    conf["current_version"] = p.perform()
    cf.save_conf(conf)
