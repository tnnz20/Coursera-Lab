from cv2 import exp
from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = 'Lovelace, Ada'
        expected = 'Ada Lovelace'
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ''
        expected = ''
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_double_name(self):
        testcase = 'Hammlet, Grace N.'
        expected = 'Grace N. Hammlet'
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = 'Violate'
        expected = 'Violate'
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()