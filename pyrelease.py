# -*- coding:utf8 -*-

import sys
import os
import json
import re

VERSION = "0.0.0"

CONF_FILENAME = "pyrelease.conf"

FORMAT = r'\d+\.\d+\.\d+\-\d+'  # <major>.<minor>.<patch>-<build>

BUILD = 3
PATCH = 2
MINOR = 1
MAJOR = 0

class Conf:
    """
    This represents a config.
    It also generates a config when there is none
    """
    def __init__(self, fname=CONF_FILENAME):
        self.fname = fname

    def gen_config(self):
        conf = {
            "files": [
            {
                "path":"put on file path here",
                "pattern": FORMAT
            },
            {
                "path":"put another file path here",
                "pattern": FORMAT
            }
            ]
        }
        with open(self.fname, 'w+') as f:
            f.write(json.dumps(conf, indent=2))

    def set(self, conf):
        if(conf is not None):
            with open(self.fname, 'w+') as f:
                f.write(json.dumps(conf, indent=2))

    def get(self):
        if(os.path.exists(self.fname)):
            with open(self.fname, 'r') as f:
                return json.loads(f.read())
        else:
            self.gen_config()
            print("Found no config file. Generating. And please review it after that, it doesn't suits your needs. (Guaranteed, whichever they are)")
            sys.exit(1)

def split_version_string(version_string):
    version = version_string.split('-')
    v = version[0].split('.')
    v.append(version[1])
    return v

def join_version_string(v):
    version = ""
    for ver in v[:-1]:
        version += ver + '.'
    version = version[:-1]
    version += "-" + v[3]
    return version

def incr(what, version):
    version[what] = str(int(version[what]) + 1)
    if(what <= PATCH):  # FIXME: redo that more clean
        version[BUILD] = '0'
        if(what <= MINOR):
            version[PATCH] = '0'
            if(what == MAJOR):
                version[MINOR] = '0'
    return version


def perform_version_incr(what, match, content, f):
    version = split_version_string(match)
    version = incr(what, version)
    new_version_string = join_version_string(version)
    content = content.replace(match, new_version_string)
    f.seek(0, 0)
    f.write(content)
    return new_version_string

def incr_version(conf, what=BUILD):
    i = 0
    for elem in conf["files"]:
        with open(elem["path"], 'r+') as f:
            content = f.read()
            match = re.findall(elem["pattern"], content)
            if(match):
                if("last_version" in elem):
                    # perform some check on what should be replaced
                    for m in match:
                        if(elem["last_version"] == m):
                            elem["last_version"] = perform_version_incr(what, m, content, f)
                            elem["position_of_match"] = match.index(m)
                            conf["files"][i] = elem
                            return conf
                else:
                    if("position_of_match" in elem):
                        # check to position
                        m = match[elem["position_of_match"]]
                        conf["last_version"] = perform_version_incr(what, m, content, f)
                        conf["files"][i] = elem
                        return conf
                    else:
                        m = match[0]
                        conf["last_version"] = perform_version_incr(what, m, content, f)
                        conf["files"][i] = elem
                        return conf
            else:
                print("ERROR: FOUND NO MATCH FOR PATTERN %s in file %s" % (elem["pattern"], elem["path"]))
                sys.exit(1)
        i += 1


if __name__ == '__main__':
    c = Conf()
    config = c.get()
    arg = sys.argv[1]
    if(arg == "build"):
         lvl = BUILD
    elif(arg == "patch"):
        lvl = PATCH
    elif(arg == "minor"):
        lvl = MINOR
    elif(arg == "major"):
        lvl = MAJOR
    recap = ""
    if("last_version" in config):
        recap += "Was %s. " % config["last_version"]
    c.set(incr_version(config, lvl))
    recap += "Is now %s." % config["last_version"]
    print(recap)
