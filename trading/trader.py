from tools import realistic_keyboard as keyboard, realistic_mouse as mouse, utils
from classes import orders, runescape, items
from config import *

import datetime
import time
import pyautogui
import random


def find_margin(exchange, item_name):
    item = items.Item(item_name)

    slot = exchange.empty_slots[0]

    mouse.all_in_one(*slot.buy_button)
    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    try:
        x, y, z, w = pyautogui.locateOnScreen("./resources/regions/exchange/first_item.png")
    except TypeError as e:
        return Exception("Chosen item could not be found")

    keyboard.write(item.name, str)

    mouse.all_in_one(x + 10, y + 25, z - 10, w)

    mouse.all_in_one(*exchange.percent_up_button)
    mouse.all_in_one(*exchange.percent_up_button)
    mouse.all_in_one(*exchange.percent_up_button)

    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    exchange.confirm()

    exchange.empty_slots = [s for s in exchange.empty_slots if s != slot]
    order = orders.Order(slot, item, 1)

    t = datetime.datetime.now()

    while not exchange.order_completed(order):
        if (datetime.now() - t) > datetime.timedelta(seconds=10):
            exchange.abort_order()
            return None

    exchange.retrieve_items(exchange, order)

    # sell



def place_buy_order(exchange, item, amount, price):
    """ Places an order in the GE in the first available slot """

    slot = exchange.empty_slots[0]

    mouse.all_in_one(*slot.buy_button)

    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    try:
        x, y, z, w = pyautogui.locateOnScreen("./resources/regions/exchange/first_item.png")
    except TypeError as e:
        return Exception("Chosen item could not be found")

    keyboard.write(item.name, str)

    mouse.all_in_one(x+10, y+20, z-10, w+25)

    exchange.set_price(price)
    exchange.set_amount(amount)

    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    exchange.confirm()

    exchange.empty_slots = [s for s in exchange.empty_slots if s != slot]
    return orders.Order(slot, item, amount, price)


def place_sell_order(exchange, item, amount, price):
    """ Places an order in the GE in the first available slot """

    slot = exchange.empty_slots[0]

    mouse.all_in_one(*slot.sell_button)

    try:
        x, y, z, w = pyautogui.locateOnScreen(item.image)
    except TypeError as e:
        return "{0} was not found in inventory".format(item.name)

    mouse.all_in_one(x, y, z, w)

    runescape.set_price(price)
    runescape.set_amount(amount)

    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    exchange.confirm()

    exchange.empty_slots = [s for s in exchange.empty_slots if s != slot]
    return orders.Order(slot, item, amount, price)