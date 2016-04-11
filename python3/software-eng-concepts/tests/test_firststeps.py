import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

import unittest
from projects.FirstSteps import FirstSteps as fs

class RichterScaleTestCase(unittest.TestCase):
    """Tests for richter_scale()"""

    def test_richter_known_values(self):
        """Tests already know richter_scale values"""
        self.assertEqual(fs.richter_scale(r_value=1), (1995262.3149688789, 0.00047687913837688307))
        self.assertEqual(fs.richter_scale(5), (1995262314968.8828, 476.87913837688404))
        self.assertEqual(fs.richter_scale(9.1), (2.818382931264449e+18, 673609687.2046962))
        self.assertEqual(fs.richter_scale(9.2), (3.981071705534953e+18, 951498973.5982201))

        with self.assertRaises(ValueError):
            fs.richter_scale("abcdefg")

        with self.assertRaises(ValueError):
            fs.richter_scale("*/356+$%")


if __name__ == '__main__':
    unittest.main()
