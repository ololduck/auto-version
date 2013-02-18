# -*- coding:utf-8 -*-

import sys
import os
import json
import re


# Full format, aka. :<major>.<minor>.<patch>+<status>-<build>
class Full:

    FORMAT = r'\d+\.\d+\.\d+\+\w\-\d+'

    def __init__(self):
        pass

    def parse_file(self, fpath):
        pass

    def perform_major(self, version):
        pass

    def perform_minor(self, version):
        pass

    def perform_patch(self, version):
        pass

    def perform_build(self, version):
        pass

    def get_current_version(self):
        pass
