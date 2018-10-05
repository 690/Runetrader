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
                                                                 coordinates['coordinates'], '+')

            self.buy_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['buy_button'], '+')

            self.sell_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['sell_button'], '+')

            self.back_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['back_button'], '+')

            self.confirm_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['confirm_button'], '+')

            self.set_price_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['set_price_button'], '+')

            self.set_amount_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['set_amount_button'], '+')

            self.chat_window = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                 coordinates['chat_window'], '+')

            self.percent_up_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                       coordinates['percent_up_button'], '+')

            self.percent_down_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                       coordinates['percent_down_button'], '+')

            self.abort_button = utils.dynamic_coordinate_converter(self.parent_coordinates,
                                                                       coordinates['abort_button'], '+')

            self.item_slots = utils.dynamic_coordinate_converter(self.parent_coordinates, coordinates['item_slot_1'], '+'), \
                              utils.dynamic_coordinate_converter(self.parent_coordinates, coordinates['item_slot_2'], '+')

            self.first_item = utils.dynamic_coordinate_converter(parent_coordinates, "(85, 411, 5, 5)", '+')
            self.first_inv = utils.dynamic_coordinate_converter(parent_coordinates, "(752, 433, 5, 5)", '+')

            self.quantity_info = utils.dynamic_coordinate_converter(parent_coordinates, "(109, 284, 235, 20)", '+')
            self.price_info = utils.dynamic_coordinate_converter(parent_coordinates, "(139, 300, 195, 24)", '+')

            self.empty_slots = self.find_empty_slots()

    def find_empty_slots(self):
        """ Finds all instances of empty Grand exchange slots, and returns a list of GE_SLOT objects """
        return [Slot(coordinates) for coordinates in pyautogui.locateAllOnScreen("./resources/regions/exchange/slot.png")]

    def set_price(self, price):
        """ Collect all available orders """

        mouse.all_in_one(*self.set_price_button)
        time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

        keyboard.write(str(price), int)
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

        # TODO   return the data of the items collected, to this by checking the inventory before and after collecting the items, very expensive function.

        mouse.all_in_one(*self.confirm_button)

    def collect_orders(self):
        """ Collect all available orders """

        mouse.all_in_one(*self.collect_button)

    def retrieve_items(self, slot):
        """ Retrives items from a completed order """

        mouse.all_in_one(*slot.coordinates)

        time.sleep(1)

        ocr_data = ocr.get_order_info(self)

        for item_slot in self.item_slots:
            mouse.all_in_one(*item_slot)

        self.empty_slots += [slot]

        if membership:
            mouse.all_in_one(*self.back_button)

        return ocr_data

    def abort_order(self, slot):
        """ Aborts an order in progress """

        if random.randint(1, 4) == 1:
            mouse.random_move(*slot.coordinates)
            mouse.click(button="right")
            x, y = pyautogui.position()
            pos = x, y + round(self.buy_button[2]/3*2)
            mouse.random_move(*pos, 5, 5)
            mouse.click()
        else:
            mouse.all_in_one(*slot.coordinates)
            mouse.all_in_one(*self.abort_button)
            mouse.all_in_one(*self.back_button)

    def order_completed(self, slot):
        return pyautogui.locateOnScreen("./resources/regions/exchange/completed_order.png", region=slot.coordinates) is not None

