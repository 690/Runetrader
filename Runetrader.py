from tools import builder
from classes import runescape, items
from lib import basic_functions as ef

import os

if __name__ == "__main__":
    """ Run the complete program """

    if not os.path.exists("./data/dynamic_coordinates.json"):
        builder.first_run()

    # Find and instantiate client and objects

    hwnd, coordinates = runescape.find_window()
    client = runescape.RunescapeInstance(hwnd, coordinates)

    dr = items.Item("Mithril bar")


    ef.place_buy_order(client.exchange, dr, 1, 277)