# -*- coding:utf-8 -*-

import sys
import os
import json
import re

SYS_EXIT_CONF_CREATED = 10


class ConfFileManager:

    FNAME = "auto_versionning.conf"

    def __init__(self):
        if(os.path.exists(self.FNAME)):
            # then read
            pass
        else:
            # then create
            pass
            conf = {}
            conf["last_version"] = None
            conf["files"] = [{"path":"path/to/file", "format":"full"},
                            {"path":"path/to/file", "format":"full"}]

            with open(self.FNAME, 'w+') as f:
                f.write(json.dumps(conf))
            sys.exit(SYS_EXIT_CONF_CREATED)


# Full format, aka. :<major>.<minor>.<patch>+<status>-<build>
class Full:

    FORMAT = r'\d+\.\d+\.\d+\+\w\-\d+'

    def __init__(self):
        pass

    def parse_file(self, fpath):
        pass

    def perform_major(self):
        pass

    def perform_minor(self):
        pass

    def perform_patch(self):
        pass

    def perform_build(self):
        pass
