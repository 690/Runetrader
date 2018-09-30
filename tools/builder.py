from tools import realistic_mouse as mouse, realistic_keyboard as keyboard, utils
from classes import runescape
import pyautogui
import json
import time


def first_run():
    hwnd, coordinates = runescape.find_window()
    client = runescape.RunescapeInstance(hwnd, coordinates)

    """ Ignore this mess, its a hardcoded image detection based automation script to place an infeasable order,
    and thus be able to collect coordinate data about every button that comes up  """

    coordinates = pyautogui.locateOnScreen('./resources/regions/exchange/exchange_window.png',region=client.coordinates)
    buy_button = pyautogui.locateOnScreen('./resources/regions/exchange/buy_button.png', region=coordinates)
    sell_button = pyautogui.locateOnScreen('./resources/regions/exchange/sell_button.png', region=coordinates)

    t = buy_button
    mouse.all_in_one(*t)

    time.sleep(1)

    back_button = pyautogui.locateOnScreen('./resources/regions/exchange/back_button.png',region=coordinates)
    confirm_button = pyautogui.locateOnScreen('./resources/regions/exchange/confirm_button.png', region=coordinates)
    set_amount_button, set_price_button = list(pyautogui.locateAllOnScreen('./resources/regions/exchange/set_price_button.png',region=coordinates))[:2]
    percent_up_button = pyautogui.locateOnScreen('./resources/regions/exchange/procent_up_button.png',region=coordinates)
    percent_down_button = pyautogui.locateOnScreen('./resources/regions/Exchange/procent_down_button.png',region=coordinates)
    x,y,z,w = pyautogui.locateOnScreen("./resources/regions/exchange/first_item.png")
    keyboard.write("Mithril bar", str)
    mouse.all_in_one(x+10,y+5,z,w)
    mouse.all_in_one(*set_price_button)
    time.sleep(1)
    keyboard.write(1, int)
    time.sleep(1)
    keyboard.press("enter")
    mouse.all_in_one(*confirm_button)
    time.sleep(1)
    try:
        mouse.all_in_one(*pyautogui.locateOnScreen("./resources/regions/chat/trade.png"))
        mouse.all_in_one(*back_button)
    except TypeError as e:
        pass
    chat_window = pyautogui.locateOnScreen('./resources/regions/chat/chat_window.png', region=client.coordinates)
    mouse.all_in_one(*t)
    time.sleep(1)
    item_slot_1, item_slot_2 = list(pyautogui.locateAllOnScreen('./resources/regions/exchange/item_slot.png',region=coordinates))[:2]
    abort_button = pyautogui.locateOnScreen('./resources/regions/Exchange/abort_button.png',region=coordinates)

    mouse.all_in_one(*abort_button)
    mouse.all_in_one(*back_button)
    time.sleep(1)
    collect_button = pyautogui.locateOnScreen('./resources/regions/Exchange/collect_button.png',region=coordinates)
    mouse.all_in_one(*collect_button)

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

            "chat_window" : "{0}".format(
                utils.dynamic_coordinate_converter(client.coordinates, chat_window, '-')),

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


    json.dump(dynamic_coordinates, open("./data/dynamic_coordinates.json", 'w'))
