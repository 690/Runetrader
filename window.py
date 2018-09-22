import pyautogui
import realistic_mouse as mouse
import realistic_keyboard as keyboard

import random
import time

from config import MEDIUM_DELAY_RANGE


def get_available_slots():
    return list(pyautogui.locateAllOnScreen("resources/ge/buy_button.png"))


def get_occupied_slots():
    return list(pyautogui.locateAllOnScreen("resources/ge/occupied_slot.png"))


def get_aborted_orders():
    return list(pyautogui.locateAllOnScreen("resources/ge/aborted_order.png"))


def get_completed_orders():
    return list(pyautogui.locateAllOnScreen("resources/ge/completed_order.png"))


def collect_orders():
    """ Collect all available orders """
    try:
        x, y, z, w = pyautogui.locateOnScreen('resources/ge/collect.png')
    except TypeError as e:
        return "No orders available for collection"

    mouse.all_in_one(x, y, z, w)


def set_price(price):
    """ Collect all available orders """
    try:
        x, y, z, w = list(pyautogui.locateAllOnScreen('resources/ge/set_price_button.png'))[1]

    except TypeError as e:
        return "Not in an available buy window"

    mouse.all_in_one(x, y, z, w)
    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    keyboard.write(str(price))
    keyboard.press("enter")


def set_amount(amount):
    """ Collect all available orders """
    try:
        x, y, z, w = list(pyautogui.locateAllOnScreen('resources/ge/set_price_button.png'))[0]
    except TypeError as e:
        print( "Not in an available buy window")

    mouse.all_in_one(x, y, z, w)
    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    keyboard.write(str(amount), int)
    keyboard.press("enter")


def place_order(item_name, amount, price):
    """ Places an order in the GE in the first available slot """
    try:
        x, y, z, w = get_available_slots()[0]
        print(x,y)
    except TypeError as e:
        return "No available GE slots"

    mouse.all_in_one(x, y, z, w)

    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))
    keyboard.write(item_name, int)

    try:
        x, y, z, w = pyautogui.locateOnScreen("resources/ge/first_item.png")
        mouse.all_in_one(x+25, y+30, z, w-10)
    except TypeError as e:
        return "No items called {0}".format(item_name)

    set_price(price)
    set_amount(amount)

    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    try:
        x, y, z, w = pyautogui.locateOnScreen("resources/ge/confirm_button.png")
        mouse.all_in_one(x, y, z, w)
    except TypeError as e:
        return "Cant place order"


if __name__ == "__main__":
    """  """
    place_order('Fire rune', 1, 10)