import window
import pyautogui
import time
import random
from tools import realistic_mouse as mouse
from tools import realistic_keyboard as keyboard
from tools import item_database
from config import *

class Slot:

    def __init__(self, coordinates):
        self.coordinates = coordinates

        self.buy_button = pyautogui.locateOnScreen('./resources/ge/buy_button.png', region=self.coordinates)
        self.sell_button = pyautogui.locateOnScreen('./resources/ge/sell_button.png', region=self.coordinates)


class Exchange:

    def __init__(self, parent_coordinates):

        self.parent_coordinates = parent_coordinates
        try:
            self.coordinates = pyautogui.locateOnScreen('./resources/ge/exchange.png', region=self.parent_coordinates)
            print("Exchange coordinates:", self.coordinates)

        except TypeError as e:
            print("Couldnt find exchange")


        print("\nFinding empty order slots")
        self.empty_slots = self.find_empty_slots()
        print(self.empty_slots)


        mouse.all_in_one(*self.empty_slots[0].buy_button)

        try:
            print("\nFinding Exchange Button locations")
            self.back_button = pyautogui.locateOnScreen('./resources/ge/back_button.png', region=self.coordinates)
            self.confirm_button = pyautogui.locateOnScreen('./resources/ge/confirm_done_button.png', region=self.coordinates)
            self.set_amount_button, self.set_price_button = \
                list(pyautogui.locateAllOnScreen('./resources/ge/set_price_button.png', region=self.coordinates))[:2]
            print("\n Finding search inventory")
            self.search_inventory = pyautogui.locateOnScreen('./resources/ge/search_inventory.png',
                                                                 region=self.parent_coordinates)

            mouse.all_in_one(*self.back_button)
        except TypeError as e:
            print('Could not find buttons in Open order window')

    def find_empty_slots(self):
        """ Finds all instances of empty Grand exchange slots, and returns a list of GE_SLOT objects """

        GE_SLOTS = pyautogui.locateAllOnScreen("./resources/ge/slot.png", region=self.coordinates)
        return [Slot(coordinates) for coordinates in GE_SLOTS]

    def set_price(self, price):
        """ Collect all availablae orders """

        x, y, z, w = self.set_price_button

        mouse.all_in_one(x, y, z, w)
        time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

        keyboard.write(str(price))
        keyboard.press("enter")

    def set_amount(self, amount):
        """ Collect all available orders """

        x, y, z, w = self.set_amount_button

        mouse.all_in_one(x, y, z, w)
        time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

        keyboard.write(str(amount), int)
        keyboard.press("enter")

    def confirm(self):
        """ Confirms the trade-in-progress """

        print(self.confirm_button)
        mouse.all_in_one(*self.confirm_button)

    def collect_orders(self):
        """ Collect all available orders """
        try:
            x, y, z, w = pyautogui.locateOnScreen('./resources/ge/collect.png')
        except TypeError as e:
            print("No orders available for collection")

        mouse.all_in_one(x, y, z, w)
