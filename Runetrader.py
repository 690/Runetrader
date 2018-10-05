import os

from lib import basic_functions as rt
from classes import runescape
from tools import builder, utils


if __name__ == "__main__":
    """ Start Runetrader"""

    if not os.path.exists("./data/dynamic_coordinates.json"):
        builder.first_run()

    # Find and instantiate client and objects

    hwnd, coordinates = runescape.find_window()
    client = runescape.RunescapeInstance(hwnd, coordinates)

    while True:
        """ Main event loop """

        items = rt.find_items()

        for item in items:
            p1, p2 = rt.find_margin(client, item)
            margin = p1 - p2
            print(margin)
            ratio = p2 / margin

            if ratio not in range(1, 20):
                continue

            print(ratio)
