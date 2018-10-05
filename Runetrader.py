from tools import builder, realistic_mouse as mouse, utils
from classes import runescape, items
import os, random
import pyautogui
from lib import basic_functions as ef

if __name__ == "__main__":
    """ Run the complete program """

    if not os.path.exists("./data/dynamic_coordinates.json"):
        builder.first_run()

    # Find and instantiate client and objects

    hwnd, coordinates = runescape.find_window()
    client = runescape.RunescapeInstance(hwnd, coordinates)


    input()

    dr = items.Item("uncut emerald")
    #for item in [random.choice(open("./data/custom/good_items.txt", 'r').readlines()) for x in range(1)]:

    margin = ef.find_margin(client, dr)
    print(margin)
