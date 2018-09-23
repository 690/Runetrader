import pyautogui
from tools import realistic_keyboard as keyboard, realistic_mouse as mouse
from classes import GE
import os
import random
import time
from config import MEDIUM_DELAY_RANGE


def get_ge_slots():
    """ Finds all instances of empty Grand exchange slots, and returns a list of GE_SLOT objects """

    GE_SLOTS = pyautogui.locateAllOnScreen("resources/ge/slot.png")
    return [GE.GE_SLOT(coordinates) for coordinates in [*GE_SLOTS]]


def get_buy_slot(region):
    return pyautogui.locateOnScreen('resources/ge/buy_button.png', region=region)


def get_sell_slot(region):
    return pyautogui.locateOnScreen('resources/ge/sell_button.png', region=region)


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
        return "Not in an available buy window"

    mouse.all_in_one(x, y, z, w)
    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    keyboard.write(str(amount), int)
    keyboard.press("enter")


def retrieve_item(itemID):
    """ Retrieves and item from the Grand exchange """

    for i in range(2):
        try:
            x, y, z, w = list(pyautogui.locateAllOnScreen('resources/ge_inventory/{0}.png'.format(itemID)))[0]

        except TypeError as e:
            print("Cannot find item in Grand exchange")
            return

        mouse.all_in_one(x, y, z, w)
        time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    for image_name in os.listdir("resources/statics/coins"):

        try:
            x, y, z, w = list(pyautogui.locateAllOnScreen('resources/statics/image_name'))[0]
            mouse.all_in_one(x, y, z, w)
            break

        except TypeError as e:
            print("No coins of this type found")


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

if __name__ == "__main__":
    print(find_slots())