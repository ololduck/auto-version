import unittest
from pyver_auto import styles

import os
import json
import re

# class ConfigTest(unittest.TestCase):
#     def setUp(self):
#         self.conf_backup = ""
#         if(os.path.exists(styles.ConfFileManager.FNAME)):
#             self.was_present = True
#             os.remove(styles.ConfFileManager.FNAME)
#             with open(styles.ConfFileManager.FNAME, 'r') as f:
#                 self.conf_backup = f.read()
#         self.a = styles.ConfFileManager()



#     def tearDown(self):
#         os.remove(self.a.FNAME)
#         if(self.was_present):
#             with open(self.a.FNAME, 'w+') as f:
#                 f.write(self.conf_backup)


#     def test_ConfCreation(self):
#         self.assertEqual(os.path.exists(self.a.FNAME), True)

#     def test_sample_content(self):
#         conf = {}
#         conf["last_version"] = None
#         conf["files"] = [{"path":"path/to/file", "format":"full"},
#                         {"path":"path/to/file", "format":"full"}]
#         conf_read = ""
#         with open(self.a.FNAME, 'r') as f:
#             conf_read = f.read()

#         self.assertEqual(json.dumps(conf), json.dumps(json.loads(conf_read)))


class StyleFullTest(unittest.TestCase):
    def setUp(self):
        self.version = ""

    def test_correct(self):

