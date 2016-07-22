import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

import unittest
from projects.Control import Control as cn

class MakingChangeTestCases(unittest.TestCase):
    """Test cases for the making_function in the Control module."""

    def test_making_change_known_output(self):
        "Tests a few known output values."
        pass


    def test_is_multiple_known_output(self):
        "Tests the known output of is_multiple() function."
        self.assertTrue(cn.is_multiple(2,4))
        self.assertFalse(cn.is_multiple(3,4))

if __name__ == '__main__':
    unittest.main()
