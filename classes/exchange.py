import pyautogui
import random
import time
import json
import os

from config import *
from tools import realistic_mouse as mouse
from tools import realistic_keyboard as keyboard
from tools import utils
from tools import ocr


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

            self.chat_window = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['Exchange']['chat_window'], '+')

            self.percent_up_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                       coordinates['Exchange']['percent_up_button'], '+')

            self.percent_down_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                       coordinates['Exchange']['percent_down_button'], '+')

            self.abort_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                       coordinates['Exchange']['abort_button'], '+')

            self.item_slots = utils.dynamic_coordinate_converter(self.parent_coordinates, coordinates['Exchange']['item_slot_1'], '+'), \
                              utils.dynamic_coordinate_converter(self.parent_coordinates, coordinates['Exchange']['item_slot_2'], '+')

            self.first_item = utils.dynamic_coordinate_converter(parent_coordinates, "(85, 411, 5, 5)", '+')
            self.first_inv = utils.dynamic_coordinate_converter(parent_coordinates, "(752, 433, 5, 5)", '+')

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
        """ set amount of item. If the amount if low,
        press the + button instead of typing the item amount """

        if amount == 1:
            return
        elif amount < random.randint(4, 6):
            mouse.random_move(*self.amount_plus_button)
            for i in range(1, amount):
                mouse.click()
        else:
            mouse.all_in_one(*self.set_amount_button)
            time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

            keyboard.write(str(amount), int)
            keyboard.press("enter")

    def confirm(self):
        """ Confirms the trade-in-progress """

        mouse.all_in_one(*self.confirm_button)

    def collect_orders(self):
        """ Collect all available orders """

        mouse.all_in_one(*self.collect_button)

    def retrieve_items(self, slot):
        """ Retrives items from a completed order """

        mouse.all_in_one(*slot.coordinates)
        for item_slot in self.item_slots:
            mouse.all_in_one(*item_slot)

        self.empty_slots += [slot]

        if membership:
            mouse.all_in_one(*self.back_button)

    def abort_order(self, slot):
        """ Aborts an order in progress """

        if 1 == 1:
            mouse.random_move(*slot.coordinates)
            mouse.click(button="right")
            x, y = pyautogui.position()
            pos = x, y + round(self.buy_button[2]/3*2)
            mouse.random_move(*pos, 5, 5)
            mouse.click()
            mouse.all_in_one(*slot.coordinates)
        else:
            mouse.all_in_one(*slot.coordinates)
            mouse.all_in_one(*self.abort_button)

    def order_completed(self, slot):
        return pyautogui.locateOnScreen("./resources/regions/exchange/completed_order.png", region=slot.coordinates) is not None

