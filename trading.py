import window
from tools import realistic_keyboard as keyboard, realistic_mouse as mouse
import time
import pyautogui
import random
from config import *
from classes import items, orders


def place_buy_order(item, amount, price):
    """ Places an order in the GE in the first available slot """

    try:
        x, y, z, w = list(pyautogui.locateAllOnScreen("resources/ge/buy_button.png"))[0]
    except TypeError as e:
        return "No available GE slots"

    mouse.all_in_one(x, y, z, w)

    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))
    keyboard.write(item.item_name, int)

    try:
        x, y, z, w = pyautogui.locateOnScreen("resources/ge/first_item.png")
        mouse.all_in_one(x+25, y+30, z, w-10)
    except TypeError as e:
        return "No items called {0}".format(item.item_name)

    window.set_price(price)
    window.set_amount(amount)

    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    try:
        x, y, z, w = pyautogui.locateOnScreen("resources/ge/confirm_button.png")
        mouse.all_in_one(x, y, z, w)
    except TypeError as e:
        return "Cant place order"

    return orders.buy_order(item, amount, price)


def place_sell_order(item, amount, price):
    """ Places an order in the GE in the first available slot """

    try:
        x, y, z, w = list(pyautogui.locateAllOnScreen("resources/ge/sell_button.png"))[0]
    except TypeError as e:
        return "No available GE slots"

    mouse.all_in_one(x, y, z, w)


    try:
        x, y, z, w = pyautogui.locateOnScreen("resources/inventory/{0}.png".format(item.image_name))
        print(x,y)
    except TypeError as e:
        return "{0} was not found in inventory".format(item.image_name)

    mouse.all_in_one(x, y, z, w)

    window.set_price(price)
    window.set_amount(amount)

    time.sleep(random.uniform(*MEDIUM_DELAY_RANGE))

    try:
        x, y, z, w = pyautogui.locateOnScreen("resources/ge/confirm_button.png")
        mouse.all_in_one(x, y, z, w)
    except TypeError as e:
        return "Cant place order"

    return orders.sell_order(item, amount, price)


if __name__ == "__main__":
    item_to_sell = items.item('air rune')
    place_sell_order(item_to_sell, 1, 6)