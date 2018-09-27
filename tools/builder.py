from tools import realistic_mouse as mouse, realistic_keyboard as keyboard, utils
from classes import runescape
import pyautogui
import json
import time


def first_run():
    hwnd, coordinates = runescape.find_window()
    client = runescape.RunescapeInstance(hwnd, coordinates)

    # Exchange coordinates

    coordinates = pyautogui.locateOnScreen('./resources/regions/exchange/exchange_window.png',region=client.coordinates)
    buy_button = pyautogui.locateOnScreen('./resources/regions/exchange/buy_button.png', region=coordinates)
    sell_button = pyautogui.locateOnScreen('./resources/regions/exchange/sell_button.png', region=coordinates)

    t = buy_button
    mouse.all_in_one(*t)

    back_button = pyautogui.locateOnScreen('./resources/regions/exchange/back_button.png',region=coordinates)
    confirm_button = pyautogui.locateOnScreen('./resources/regions/exchange/confirm_button.png', region=coordinates)
    set_amount_button, set_price_button = list(pyautogui.locateAllOnScreen('./resources/regions/exchange/set_price_button.png',region=coordinates))[:2]
    time.sleep(0.25)
    search_inventory = pyautogui.locateOnScreen('./resources/regions/chat/g.png',region=client.coordinates)

    percent_up_button = pyautogui.locateOnScreen('./resources/regions/exchange/procent_up_button.png',region=coordinates)
    percent_down_button = pyautogui.locateOnScreen('./resources/regions/Exchange/procent_down_button.png',region=coordinates)


    keyboard.write("Mithril bar", str)
    x,y,z,w = pyautogui.locateOnScreen("./resources/regions/exchange/first_item.png")
    mouse.all_in_one(x+10,y+5,z,w)
    mouse.all_in_one(*set_price_button)
    keyboard.write(1, int)
    keyboard.press("enter")
    mouse.all_in_one(*confirm_button)
    mouse.all_in_one(*t)


    item_slot_1, item_slot_2 = list(pyautogui.locateAllOnScreen('./resources/regions/exchange/item_slot.png',region=coordinates))[:2]
    abort_button = pyautogui.locateOnScreen('./resources/regions/Exchange/abort_button.png',region=coordinates)

    mouse.all_in_one(*abort_button)
    for item_slot in [item_slot_1, item_slot_2]:
        mouse.all_in_one(*item_slot)

    mouse.all_in_one(*back_button)


    dynamic_coordinates = {

        "Exchange": {
            "coordinates" : "{0}".format(
                client.coordinates, coordinates),

            "buy_button" : "{0}".format(
                utils.dynamic_coordinate_converter(client.coordinates, buy_button, '-')),

            "sell_button": "{0}".format(
                utils.dynamic_coordinate_converter(client.coordinates, sell_button, '-')),

            "back_button": "{0}".format(
                utils.dynamic_coordinate_converter(client.coordinates, back_button, '-')),

            "confirm_button": "{0}".format(
                utils.dynamic_coordinate_converter(client.coordinates, confirm_button, '-')),

            "set_amount_button": "{0}".format(
                utils.dynamic_coordinate_converter(client.coordinates, set_amount_button, '-')),

            "set_price_button": "{0}".format(
                utils.dynamic_coordinate_converter(client.coordinates, set_price_button, '-')),

            "search_inventory" : "{0}".format(
                utils.dynamic_coordinate_converter(client.coordinates, search_inventory, '-')),

            "percent_up_button": "{0}".format(
                utils.dynamic_coordinate_converter(client.coordinates, percent_up_button, '-')),

            "percent_down_button": "{0}".format(
                utils.dynamic_coordinate_converter(client.coordinates, percent_down_button, '-')),

            "abort_button": "{0}".format(
                utils.dynamic_coordinate_converter(client.coordinates, abort_button, '-')),

            "item_slot_1" : "{0}".format(
                utils.dynamic_coordinate_converter(client.coordinates, item_slot_1, '-')),

            "item_slot_2": "{0}".format(
                utils.dynamic_coordinate_converter(client.coordinates, item_slot_2, '-')),

        }
    }

    with open('./data/dynamic_coordinates.json', 'w') as f:
        json.dump(dynamic_coordinates, f)

