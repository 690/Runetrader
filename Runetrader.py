from tools import builder
from classes import runescape
from classes import states
import os


if __name__ == "__main__":
    """ Run the complete program """

    if not os.path.exists("./data/dynamic_coordinates.json"):
        """ If there is no existing file containing the dynamic coordinates for windows and the buttons therein:
            run a Runescape instance, locate positions and store them """

        builder.first_run()

    # Find and instantiate client and objects

    hwnd, coordinates = runescape.find_window()
    client = runescape.RunescapeInstance(hwnd, coordinates)


    state = input("\n: ")

    states.op_dict[state](client)
