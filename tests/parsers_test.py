import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import unittest
from auto_version import parsers


class TestBasicParser(unittest.TestCase):

    p = None

    def setUp(self):
        self.conf = {"files": ["testfile1.txt", "testfile2.txt"], "style": "Doublet", "action": "minor", "current_version": "0.0", "commit": False}
        for f in self.conf["files"]:
            with open(f, 'w+') as fd:
                fd.write(""""version = '0.0'\n""")

    def tearDown(self):
        if(type(self.conf["files"]) is list or type(self.conf["files"]) is tuple):
            for f in self.conf["files"]:
                os.remove(f)
        else:
            os.remove(self.conf["files"])
        if(os.path.exists("testing_dir") and os.path.isdir("testing_dir")):
            os.rmdir("testing_dir")

    def test_insanciation(self):
        self.p = parsers.BasicParser(self.conf)
        self.assertIsInstance(self.p, parsers.BasicParser)

    def test_single_file_instanciation(self):
        files = self.conf["files"]
        self.conf["files"] = "testfile1.txt"
        self.p = parsers.BasicParser(self.conf)
        self.assertIsInstance(self.p, parsers.BasicParser)
        self.conf["files"] = files

    def test_directory_instanciation(self):
        os.mkdir("testing_dir")
        self.assertRaises(NotImplementedError, parsers.BasicParser, self.conf)
        os.rmdir("testing_dir")

    def test_no_files_instanciation(self):
        self.assertRaises(ValueError, parsers.BasicParser, self.conf)

    def test_perform(self):
        if(self.p is None):
            self.test_insanciation()
        self.assertEqual("0.1", self.p.perform())

if __name__ == '__main__':
    unittest.main()
