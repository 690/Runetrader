from tools import realistic_mouse as mouse, utils
from classes import runescape
import pyautogui
import json


def first_run():
    hwnd, coordinates = runescape.find_window()
    client = runescape.RunescapeInstance(hwnd, coordinates)

    # Exchange coordinates

    coordinates = pyautogui.locateOnScreen('./resources/regions/exchange/exchange_window.png',region=client.coordinates)
    buy_button = pyautogui.locateOnScreen('./resources/regions/exchange/buy_button.png', region=coordinates)
    sell_button = pyautogui.locateOnScreen('./resources/regions/exchange/sell_button.png', region=coordinates)

    mouse.all_in_one(*buy_button)

    back_button = pyautogui.locateOnScreen('./resources/regions/exchange/back_button.png',region=coordinates)
    confirm_button = pyautogui.locateOnScreen('./resources/regions/exchange/confirm_button.png', region=coordinates)
    set_amount_button, set_price_button = list(pyautogui.locateAllOnScreen('./resources/regions/exchange/set_price_button.png',region=coordinates))[:2]
    search_inventory = pyautogui.locateOnScreen('./resources/regions/chat/g.png',region=client.coordinates)

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
                utils.dynamic_coordinate_converter(client.coordinates, search_inventory, '-'))
        }
    }

    with open('./data/dynamic_coordinates.json', 'w') as f:
        json.dump(dynamic_coordinates, f)

