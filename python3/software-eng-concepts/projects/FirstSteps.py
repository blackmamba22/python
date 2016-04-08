

class FirstSteps:
    """Basic python programs to get started."""

    def __init__(self):
        pass

    @staticmethod
    def richter_scale():
        """
        Prompt user to enter a richter scale # and perform calculations to
        display equivalent amount of energy in joules and in tons of exploded TNT.
        """
        user_input = input("Enter a richter scale value: ")
        energy_in_joules = -1
        num_tons_tnt_exploded = -1

        try:
            richter_scale_val = float(user_input)
            energy_in_joules = 10**((1.5 * richter_scale_val) + 4.8)
            num_tons_tnt_exploded = energy_in_joules / (4.184 * 10**9)
        except Exception as e:
            print (e)
        finally:
            print ("\nEnergy in Joules = {0:.2f}\nNumber tons of TNT exploded = {1:.2f}"
                .format(energy_in_joules, num_tons_tnt_exploded) )
            return (energy_in_joules, num_tons_tnt_exploded)
