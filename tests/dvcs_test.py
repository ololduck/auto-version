import os
import sys
import re
sys.path.insert(0, os.path.abspath('..'))

import unittest
from subprocess import check_output, check_call, CalledProcessError

from auto_version import dvcs, utils

class GitTest(unittest.TestCase):
    def setUp(self):
        check_call(["git", "init", "testing_repo"])
        os.chdir(os.path.abspath('testing_repo'))
        with open("hello", 'w+') as f:
            f.write("VERSION = 0.0.1")
        check_call(["git", "add", "hello"])
        check_call(["git", "commit", "-m", "Initial Commit"])
        check_call(["git", "tag", "0.0.1"])
        self.git = dvcs.Git()
        self.git.style = utils.import_style("Triplet")

    def tearDown(self):
        os.chdir(os.path.abspath('..'))
        check_call(["rm", "-rf", "testing_repo"])
        self.git = None

    def test_get_version(self):
        self.assertEqual("0.0.1", str(self.git.get_current_version(with_status=False, increment=False)))
        self.assertEqual("0.0.1", str(self.git.get_current_version(with_status=False, increment=True)))
        self.assertEqual("0.0.1", str(self.git.get_current_version(with_status=True,increment=False)))
        self.assertEqual("0.0.1", str(self.git.get_current_version(with_status=True,increment=True)))

    def test_dirty_get_version(self):
        with open("hello", 'a') as f:
            f.write("\nHi!")
        check_call(["git", "commit","-am", "Modified something"])
        self.assertEqual("0.0.1", str(self.git.get_current_version(with_status=False, increment=False)))
        self.assertEqual("0.0.2", str(self.git.get_current_version(with_status=False, increment=True)))
        self.assertNotEqual("0.0.1", str(self.git.get_current_version(with_status=True, increment=False)))
        self.assertNotEqual("0.0.2", str(self.git.get_current_version(with_status=True, increment=True)))
        regex = self.git.style("0.0.0").__format__ + r"\-pre\d+\-\d{8,10}"
        value = self.git.get_current_version(with_status=True, increment=False)
        self.assertNotEqual(None, re.match(regex, value))


if __name__ == '__main__':
    unittest.main()
