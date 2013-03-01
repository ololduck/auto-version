import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import unittest
from auto_version import styles


class StyleTripletTest(unittest.TestCase):

    def test_correct_increment(self):
        self.t = styles.Triplet("1.2.3")
        self.assertEqual("1.2.4", self.t.increment("patch"))
        self.assertEqual("1.3.0", self.t.increment("minor"))
        self.assertEqual("2.0.0", self.t.increment("major"))

    def test_not_correct_current_version(self):
        self.assertRaises(ValueError, styles.Triplet, "1-2-3")

    def test_not_correct_action(self):
        self.t = styles.Triplet("1.2.3")
        self.assertRaises(ValueError, self.t.increment, "ohai")

    def test_version_string_epuration(self):
        self.assertEqual("1.2.3", styles.BaseStyle.get_pure_version_string(styles.Triplet, "v1.2.3"))

        self.assertEqual("1.2.3", styles.BaseStyle.get_pure_version_string(styles.Triplet, "1.2.3"))


class StyleDoubletTest(unittest.TestCase):

    def test_correct_increment(self):
        self.t = styles.Doublet("1.2")
        self.assertEqual("1.3", self.t.increment("minor"))
        self.assertEqual("2.0", self.t.increment("major"))

    def test_not_correct_current_version(self):
        self.assertRaises(ValueError, styles.Doublet, "1-2")

    def test_not_correct_action(self):
        self.t = styles.Doublet("1.2")
        self.assertRaises(ValueError, self.t.increment, "ohai")

    def test_version_string_epuration(self):
        self.assertEqual("1.2", styles.BaseStyle.get_pure_version_string(styles.Doublet, "v1.2"))

        self.assertEqual("1.2", styles.BaseStyle.get_pure_version_string(styles.Doublet, "1.2"))


class StyleRevisionTest(unittest.TestCase):

    def test_correct_increment(self):
        self.t = styles.Revision("r1")
        self.assertEqual("r2", self.t.increment("blblbl"))
        self.assertEqual("r2", self.t.increment())

    def test_not_correct_current_version(self):
        self.assertRaises(ValueError, styles.Revision, "1")

    def test_version_string_epuration(self):
        self.assertEqual("r1", styles.BaseStyle.get_pure_version_string(styles.Triplet, "revr1"))

        self.assertEqual("r1", styles.BaseStyle.get_pure_version_string(styles.Triplet, "r1"))


if __name__ == '__main__':
    unittest.main()
