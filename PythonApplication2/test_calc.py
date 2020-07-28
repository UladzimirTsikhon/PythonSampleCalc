import unittest
import sys
from calc import calc

class Test_test_1(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc(4,5).add(),9)
    def test_mul(self):
        self.assertEqual(calc(4,5).mul(),1)
    def test_sub(self):
        self.assertEqual(calc(4,5).sub(),2)
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()
