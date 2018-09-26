import pyautogui
import os
import random
import time
import win32gui

from tools import realistic_mouse as mouse
from config import MEDIUM_DELAY_RANGE
from classes import exchange


def find_window(name="RuneLite"):
    """ Find coordinates for a given window """

    hwnd = win32gui.FindWindow(None, name)
    coordinates = win32gui.GetWindowRect(hwnd)
    print(hwnd, coordinates)
    return hwnd, coordinates


class RunescapeInstance:
    """ Instance of the Runescape window """

    def __init__(self, hwnd, coordinates):
        self.hwnd = hwnd
        self.coordinates = coordinates

        print("Creating a Grand Exchange object")
        self.exchange = exchange.Exchange(self.coordinates)


def tab_switcher():
    """ Randomly switches tabs and interacts in the sidebar """

    tab = "inventory_tab.png"

    for i in random.sample(os.listdir("resources/regions/sidebar/tabs"), len(os.listdir("resources/regions/sidebar/tabs"))):
        if i != tab:
            tab = i
            break

    try:
        x, y, z, w = pyautogui.locateOnScreen("resources/regions/sidebar/tabs/{0}".format(tab))
        mouse.all_in_one(x, y, z, w)
    except TypeError as e:
        return "Cannot go to tab {0}".format(tab)

    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    try:
        x, y, z, w = pyautogui.locateOnScreen("resources/regions/sidebar/tabs/inventory_tab.png")
        mouse.all_in_one(x, y, z, w)
    except TypeError as e:
        return "Cannot go to tab inventory_tab"
