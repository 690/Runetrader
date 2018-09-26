from classes import items
import window
import trading
import time

hwnd, coordinates = window.find_runescape_window()
client = window.RunescapeInstance(hwnd, coordinates)


m_bar = items.Item("Mithril bar")
order = trading.place_buy_order(client.exchange, m_bar, 10, 811)
