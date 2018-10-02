from tools import realistic_mouse as mouse, realistic_keyboard as keyboard
from classes import orders, items
import pyautogui
import datetime


def find_margin(client, item):

    exchange = client.exchange

    slot = exchange.empty_slots[0]
    exchange.empty_slots = [s for s in exchange.empty_slots if s != slot]

    mouse.all_in_one(*slot.buy_button)

    keyboard.write(item.name)

    mouse.all_in_one(*exchange.first_item)

    mouse.random_move(*exchange.percent_up_button)
    mouse.click()
    mouse.click()
    mouse.click()

    exchange.confirm()

    time = datetime.datetime.now()
    while not exchange.order_completed(slot):
        if time < datetime.datetime.today() - datetime.timedelta(hours=1):
            exchange.abort_order(slot)
            return

    client.inventory.add(item, 1)
    exchange.retrieve_items(slot)

    mouse.all_in_one(*slot.sell_button)

    mouse.all_in_one(*client.inventory.find(item).coordinates)

    mouse.random_move(*exchange.percent_down_button)
    mouse.click()
    mouse.click()
    mouse.click()

    exchange.confirm()

    time = datetime.datetime.now()
    while not exchange.order_completed(slot):
        if time < datetime.datetime.today() - datetime.timedelta(hours=1):
            exchange.abort_order(slot)
            return

    client.inventory.remove(item, 1)
    exchange.retrieve_items(slot)

def place_buy_order(client, item, amount, price):
    exchange = client.exchange

    slot = exchange.empty_slots[0]
    exchange.empty_slots = [s for s in exchange.empty_slots if s != slot]

    mouse.all_in_one(*slot.buy_button)

    keyboard.write(item.name)

    mouse.all_in_one(*exchange.first_item)

    exchange.set_price(price)

    exchange.set_amount(amount)

    exchange.confirm()

    return orders.Order(slot, item)


def place_sell_order(client, item, amount, price):
    exchange = client.exchange

    slot = exchange.empty_slots[0]
    exchange.empty_slots = [s for s in exchange.empty_slots if s != slot]

    mouse.all_in_one(*slot.sell_button)

    inventory_spot = client.inventory.find(item)
    mouse.all_in_one(*inventory_spot.coordinates)

    exchange.set_price(price)

    exchange.set_amount(amount)

    exchange.confirm()

    return orders.Order(slot, item)