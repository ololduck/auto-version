# -*- coding:utf-8 -*-

import sys
import os
import json
import re

class ConfFileManager:
    FNAME="auto_versionning.conf"
    def __init__(self):
        if(os.path.exists(self.FNAME)):
            # then read
            pass
        else:
            # then create
            pass

# Full format, aka. :<major>.<minor>.<patch>+<status>-<build>
class Full:

    FORMAT=r'\d+\.\d+\.\d+\+\w\-\d+'

    def __init__(self):
        pass

    def parse_file(self, fpath):
        pass

    def perform_major(self):
        pass

    def perform_minor(self):
        pass

