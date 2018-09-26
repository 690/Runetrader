import pyautogui
import random
import time
import json
import os

from config import *
from tools import realistic_mouse as mouse
from tools import realistic_keyboard as keyboard
from tools import utils


class Slot:

    def __init__(self, coordinates):
        self.coordinates = coordinates

        self.buy_button = pyautogui.locateOnScreen('./resources/regions/exchange/buy_button.png', region=self.coordinates)
        self.sell_button = pyautogui.locateOnScreen('./resources/regions/exchange/sell_button.png', region=self.coordinates)


class Exchange:

    def __init__(self, parent_coordinates):

        self.parent_coordinates = parent_coordinates

        if os.path.exists("./data/dynamic_coordinates.json"):

            file = open('./data/dynamic_coordinates.json', 'r')
            coordinates = json.load(file)

            self.coordinates = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['Exchange']['coordinates'], '+')

            self.buy_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['Exchange']['buy_button'], '+')

            self.sell_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['Exchange']['sell_button'], '+')

            self.back_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['Exchange']['back_button'], '+')

            self.confirm_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['Exchange']['confirm_button'], '+')

            self.set_price_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['Exchange']['set_price_button'], '+')

            self.set_amount_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['Exchange']['set_amount_button'], '+')

            self.search_inventory = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['Exchange']['search_inventory'], '+')

            self.percent_up_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                       coordinates['Exchange']['percent_up_button'], '+')

            self.percent_down_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                       coordinates['Exchange']['percent_down_button'], '+')

            print(self.coordinates)
            self.empty_slots = self.find_empty_slots()

            print("debug, exchange.py", self.empty_slots, self.coordinates)

    def find_empty_slots(self):
        """ Finds all instances of empty Grand exchange slots, and returns a list of GE_SLOT objects """
        return [Slot(coordinates) for coordinates in pyautogui.locateAllOnScreen("./resources/regions/exchange/slot.png")]

    def set_price(self, price):
        """ Collect all available orders """

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
            x, y, z, w = pyautogui.locateOnScreen('./resources/regions/exchange/collect.png')
        except TypeError as e:
            print("No orders available for collection")

        mouse.all_in_one(x, y, z, w)


    def retrieve_items(self, order):
        """ Retrives items from a completed order """


        mouse.all_in_one(*order.slot.coordinates)
        for item_spot in order.slot.item_spots:
            mouse.all_in_one(item_spot)

        self.empty_slots = self.empty_slots.append(order.slot)

    def abort_order(self, order):
        """ Aborts an order in progress """
        mouse.all_in_one(*order.slot)
        mouse.all_in_one(*pyautogui.locateOnScreen("./resources/regions/exchange/abort_button.png"))
        mouse.all_in_one(*self.back_button)
        self.retrieve_items(order)

    def order_completed(self, order):
        return pyautogui.locateOnScreen("./resources/regions/exchange/completed_order.png", region = order.slot.coordinates) is not None

