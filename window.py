import pyautogui
import realistic_mouse as mouse
import realistic_keyboard as keyboard
import os
import random
import time
import item_database
from config import MEDIUM_DELAY_RANGE



def get_available_slots():
    """ Returns a list of free Grand exchange slots """

    return list(pyautogui.locateAllOnScreen("resources/ge/buy_button.png"))


def get_occupied_slots():
    """ Returns a list of Grand exchange slots that have ongoing orders """

    return list(pyautogui.locateAllOnScreen("resources/ge/occupied_slot.png"))


def get_aborted_orders():
    """ Returns a list of Grand exchange slots that have aborted orders """

    return list(pyautogui.locateAllOnScreen("resources/ge/aborted_order.png"))


def get_completed_orders():
    """ Returns a list of Grand exchange slots that have completed orders"""

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
        return "Not in an available buy window"

    mouse.all_in_one(x, y, z, w)
    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    keyboard.write(str(amount), int)
    keyboard.press("enter")


def retrieve_item(itemID):
    """ Retrieves and item from the Grand exchange """

    for i in range(2):
        try:
            x, y, z, w = list(pyautogui.locateAllOnScreen('resources/items/{0}.png'.format(itemID)))[0]

        except TypeError as e:
            print("Cannot find item in Grand exchange")
            return

        mouse.all_in_one(x, y, z, w)
        time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    for i, coin in range(item_database.lookup("coins")):

        try:
            x, y, z, w = list(pyautogui.locateAllOnScreen('resources/items/{0}'.format(coin['image_name'])))[0]
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
