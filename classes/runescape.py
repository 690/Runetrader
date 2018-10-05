import pyautogui
import os
import random
import time
import win32gui
import json
import config

from tools import realistic_mouse as mouse, utils, ocr
from classes import exchange, items
from classes.inventory import  Inventory


def find_window(name="RuneLite"):
    """ Returns handle and coordinates for a given window """

    hwnd = win32gui.FindWindow(None, name)
    coordinates = win32gui.GetWindowRect(hwnd)
    print("DEBUG: Runescape client window, hwnd : {0}, coordinates : {1}".format(hwnd, coordinates))
    return hwnd, coordinates


class RunescapeInstance:
    """ Instance of the Runescape window """

    def __init__(self, hwnd, coordinates):

        print("DEBUG: setting up runescape client instance")

        self.hwnd = hwnd
        self.coordinates = coordinates

        self.exchange = exchange.Exchange(self.coordinates)
        self.is_member = config.membership

        if os.path.exists("./data/dynamic_coordinates.json"):

            file = open('./data/dynamic_coordinates.json', 'r')
            coords = json.load(file)

            self.inventory = Inventory(utils.dynamic_coordinate_converter(self.coordinates,
                                                                          coords['inventory_window'], '+'))
        self.inventory.inventory_list[0].set(items.Item('coins'), self.find_coins())
        print("DEBUG: Coins in inventory", self.inventory.inventory_list[0].amount)

    def find_coins(self):
        print("DEBUG: Finding coins in inventory spot 0")
        mouse.random_move(*self.inventory.inventory_list[0].coordinates)
        mouse.click('right')
        time.sleep(0.5)
        mouse.all_in_one(*pyautogui.locateOnScreen("./resources/regions/inventory/examine_coins.png"))
        try:
            return int(ocr.recognize_int(self.exchange.newest_msg))
        except TypeError as e:
            print("DEBUG: Could not find coins, returning config.GP_CAPITAL")
            return config.GP_CAPITAL

    def tab_switcher(self):
        """ Randomly switches tabs and interacts in the sidebar """

        tab = "inventory_tab.png"

        for i in random.sample(os.listdir("resources/regions/sidebar/tabs"),
                               len(os.listdir("resources/regions/sidebar/tabs"))):
            if i != tab:
                tab = i
                break

        try:
            print("DEBUG: Changing menu tab to", tab)
            x, y, z, w = pyautogui.locateOnScreen("resources/regions/sidebar/tabs/{0}".format(tab))
            mouse.all_in_one(x, y, z, w)
        except TypeError as e:
            print("Cannot go to tab {0}".format(tab))

        time.sleep(random.uniform(*config.MEDIUM_DELAY_RANGE))

        try:
            x, y, z, w = pyautogui.locateOnScreen("resources/regions/sidebar/tabs/inventory_tab.png")
            mouse.all_in_one(x, y, z, w)
        except TypeError as e:
            print("Cannot go to tab inventory_tab")
