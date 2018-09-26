import window
from tools import realistic_keyboard as keyboard, realistic_mouse as mouse
import time
import pyautogui
import random
from config import *
from classes import items, orders


def place_buy_order(exchange, item, amount, price):
    """ Places an order in the GE in the first available slot """

    slot = exchange.empty_slots[0]

    mouse.all_in_one(*slot.buy_button)

    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    try:
        x, y, z, w = pyautogui.locateOnScreen("./resources/regions/exchange/first_item.png")

    except TypeError as e:
        print("{0} was not found in GE".format(item.name))
        return Exception("Chosen item could not be found")


    keyboard.write(item.name, str)

    print(exchange.parent_coordinates)

    print("\n Trying to find item", item.name)



    mouse.all_in_one(x, y, z, w+25)

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

    window.set_price(price)
    window.set_amount(amount)

    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    exchange.confirm()

    exchange.empty_slots = [s for s in exchange.empty_slots if s != slot]
    return orders.Order(slot, item, amount, price)