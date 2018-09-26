from tools import process_manager
from classes import exchange
from classes import items
import window
import trading

hwnd, coordinates = window.find_runescape_window()
client = window.runescape_instance(hwnd, coordinates)


jug = items.Item("Jug")
trading.place_buy_order(client.exchange, jug, 2, 25001)
input()
trading.place_sell_order(client.exchange, jug, 2, 25999)
500