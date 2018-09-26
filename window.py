import pyautogui
from tools import realistic_keyboard as keyboard, realistic_mouse as mouse

import os
import random
import time
from config import MEDIUM_DELAY_RANGE
import math
import win32gui
from classes import exchange

def find_runescape_window():
    print("Finding coordinates for runescape window")

    hwnd = win32gui.FindWindow(None, "RuneLite")
    coordinates = win32gui.GetWindowRect(hwnd)
    print(hwnd, coordinates)
    return hwnd, coordinates


class runescape_instance:

    def __init__(self, hwnd, coordinates):
        self.hwnd = hwnd
        self.coordinates = coordinates

        print("Creating a Grand Exchange object")
        self.exchange = exchange.Exchange(self.coordinates)


def tab_switcher():

    tab = "inventory_tab.png"

    for i in random.sample(os.listdir("resources/tabs"), len(os.listdir("resources/tabs"))):
        if i != tab:
            tab = i
            break

    try:
        x, y, z, w = pyautogui.locateOnScreen("resources/tabs/{0}".format(tab))
        mouse.all_in_one(x, y, z, w)
    except TypeError as e:
        return "Cannot goto tab {0}".format(tab)

    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    try:
        x, y, z, w = pyautogui.locateOnScreen("resources/tabs/inventory_tab.png")
        mouse.all_in_one(x, y, z, w)
    except TypeError as e:
        return "Cannot goto tab inventory_tab"
