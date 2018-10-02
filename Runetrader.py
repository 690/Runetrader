from tools import builder, realistic_mouse as mouse, utils
from classes import runescape, items
import os, time
import pyautogui
from lib import basic_functions as ef

if __name__ == "__main__":
    """ Run the complete program """

    if not os.path.exists("./data/dynamic_coordinates.json"):
        builder.first_run()

    # Find and instantiate client and objects

    hwnd, coordinates = runescape.find_window()
    client = runescape.RunescapeInstance(hwnd, coordinates)

    coins = items.Item("Coins")
    client.inventory.inventory_list[0].item = coins
    dr = items.Item("Mithril bar")
    ef.find_margin(client, dr)

    """ txt_item_list = open("./data/custom/good_items.txt", 'r')
 item_list = [items.Item(item) for item in txt_item_list.readlines()[:4]]

 margins = (ef.find_margin(client.exchange, item) for item in item_list)
 for margin in margins:
     print(margin)"""