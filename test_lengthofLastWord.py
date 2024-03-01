import unittest
import stringfunction
class TestlengthofLastWOrd(unittest.TestCase):
    def test_singleword(self):
        self.assertEqual(stringfunction.lengthofLastWord("sikandar"),8)
    def test_toword(self):
        self.assertEqual(stringfunction.lengthofLastWord("AYAN khan"),4)