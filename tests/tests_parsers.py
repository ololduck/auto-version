import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import unittest
from auto_version import parsers

class TestBasicParser(unittest.TestCase):

    p = None

    def setUp(self):
        self.conf = {"files": ["testfile1.txt,", "testfile2.txt"], "style":"Doublet", "action": "minor", "current_version":"0.0"}
        for f in self.conf["files"]:
            with open(f, 'w+') as fd:
                fd.write(""""version = '0.0'\n""")

    def tearDown(self):
        for f in self.conf["files"]:
            os.remove(f)

    def test_insanciation(self):
        self.p = parsers.BasicParser(files=self.conf["files"], style=self.conf["style"], action=self.conf["action"], current_version=self.conf["current_version"])
        self.assertIsInstance(self.p, parsers.BasicParser)

    def test_perform(self):
        if(self.p is None):
            self.test_insanciation()
        self.assertEqual("0.1", self.p.perform())

if __name__ == '__main__':
    unittest.main()
