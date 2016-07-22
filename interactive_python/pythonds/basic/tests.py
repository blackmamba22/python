import os
import os.path
import sys
import unittest

from stack import Stack
from algorithms import *

sys.path.append(os.path.join(os.getcwd(), '.'))
sys.path.append(os.path.join(os.getcwd(), '..'))

def revstring(mystr):
    m = Stack()
    for s in mystr:
      m.push(s)

    reverse = ""
    while not m.isEmpty():
      reverse += m.pop()

    return reverse

class TestStackAlgorithms(unittest.TestCase):

    def setUp(self):
        pass

    def test_revstring(self):
        self.assertEqual(revstring('apple'), 'elppa')
        self.assertEqual(revstring('x'), 'x')
        self.assertEqual(revstring('1234567890'),'0987654321')

    def test_decimal_to_binary(self):
        "Tests known values for the function convert_decimal_to_binary()"
        self.assertEqual(convert_decimal_to_binary(233), "11101001")
        self.assertEqual(convert_decimal_to_binary(0), "")

    def test_base_converter(self):
        "Tests known values for the function base_converter()"

        # test for base 2
        self.assertEqual(base_converter(25, 2), "11001")

        # test for base 16
        self.assertEqual(base_converter(233, 16), "E9")

if __name__ == '__main__':
    unittest.main()
