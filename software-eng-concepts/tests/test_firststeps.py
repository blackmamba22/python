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


class WindChillTemperatureIndexTestCase(unittest.TestCase):
    """Tests for wind_chill"""

    def test_windchill_index_known_values(self):
        """Tests the known values"""
        self.assertEqual(fs.calculate_windchill_temperature_index
                                (air_temp=10.0, wind_speed=15.0), -6.5895344209562525)
        self.assertEqual(fs.calculate_windchill_temperature_index
                                (air_temp=0.0, wind_speed=25.0), -24.093780999553864)
        self.assertEqual(fs.calculate_windchill_temperature_index
                                (air_temp=-10.0, wind_speed=35.0), -41.16894662953316)

    def test_windchill_known_bad_values(self):
        """Test the input values that are guaranteed to fail."""
        with self.assertRaises(ValueError):
            fs.calculate_windchill_temperature_index(air_temp=100, wind_speed=15)

        with self.assertRaises(ValueError):
            fs.calculate_windchill_temperature_index(air_temp=25, wind_speed=2)

        with self.assertRaises(ValueError):
            fs.calculate_windchill_temperature_index(air_temp="abc", wind_speed="abc")

        with self.assertRaises(ValueError):
            fs.calculate_windchill_temperature_index(air_temp="zz5", wind_speed="10.0")

    def test_windchill_return_instance(self):
        """Test that a float type is returned"""
        self.assertIsInstance(fs.calculate_windchill_temperature_index
                                (air_temp=10.0, wind_speed=15.0), float)
if __name__ == '__main__':
    unittest.main()
