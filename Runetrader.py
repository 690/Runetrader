from classes import items, runescape
from trading import trading

hwnd, coordinates = runescape.find_window()
client = runescape.RunescapeInstance(hwnd, coordinates)
order = trading.place_buy_order(client.exchange, items.Item("Mithril bar"), 10, 800)

if __name__ == "__main__":
    """ Run the complete program """

    pass
