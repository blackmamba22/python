# -*- coding: utf-8 -*-
import sys

class FirstSteps:
    """Basic python programs to get started."""

    def __init__(self):
        pass

    @staticmethod
    def richter_scale(r_value=None):
        """
        Prompt user to enter a richter scale # and perform calculations to
        display equivalent amount of energy in joules and in tons of exploded TNT.
        """

        if r_value is None:
            user_input = input("Enter a richter scale value: ")
        else:
            user_input = r_value

        energy_in_joules = None
        num_tons_tnt_exploded = None

        try:
            richter_scale_val = float(user_input)
            energy_in_joules = 10**((1.5 * richter_scale_val) + 4.8)
            num_tons_tnt_exploded = energy_in_joules / (4.184 * 10**9)
        except ValueError:
            print ("Error: Invalid input, please enter a floating point number.")
            raise

        print ("\nEnergy in Joules = {0:.2f}\nNumber tons of TNT exploded = {1:.2f}"
            .format(energy_in_joules, num_tons_tnt_exploded) )
        return (energy_in_joules, num_tons_tnt_exploded)


    @staticmethod
    def calculate_windchill_temperature_index(air_temp=None, wind_speed=None):
        """Calculates the wind_chill temperature index."""
        if air_temp is None and wind_speed is None:
            air_temp = input("Enter air temperature in Fahrenheit: ")
            wind_speed = input("Enter wind speed in mph: ")

        wind_chill = None
        try:
            air_temp = float(air_temp)
            wind_speed = float(wind_speed)

            if not -50 < air_temp < 50:
                raise ValueError("Temperatures need to be above -50°F and at or below 50°F.")

            if not 3 < wind_speed < 110:
                raise ValueError("Wind speed need to be above 3 MPH and below 110 MPH.")

            wind_chill = 35.74 + 0.6215*(air_temp) - 35.75*(wind_speed**(0.16)) \
                            + 0.4275*(air_temp)*(wind_speed**(0.16))
        except ValueError as e:
            print (e)
            raise
        finally:
            print ("Wind Chill Temperature Index: " + str(wind_chill))
        return wind_chill
