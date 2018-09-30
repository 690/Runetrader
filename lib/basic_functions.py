from tools import realistic_mouse as mouse, realistic_keyboard as keyboard
from classes import orders
import pyautogui


def find_margin(exchange, item):

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

    while not exchange.order_completed(slot):
        pass

    exchange.retrieve_items(slot)


def place_buy_order(exchange, item, amount, price):

    slot = exchange.empty_slots[0]
    exchange.empty_slots = [s for s in exchange.empty_slots if s != slot]

    mouse.all_in_one(*slot.buy_button)

    keyboard.write(item.name)

    mouse.all_in_one(*exchange.first_item)

    exchange.set_price(price)

    exchange.set_amount(amount)

    exchange.confirm()

    exchange.abort_order(slot)

    return orders.Order(slot, item)


def place_sell_order(exchange, item, amount, price):

    slot = exchange.empty_slots[0]
    exchange.empty_slots = [s for s in exchange.empty_slots if s != slot]

    mouse.all_in_one(*slot.sell_button)

    # TODO  edit this line, to use inventory system and function inventory.get_item_coordinates()
    mouse.all_in_one(*pyautogui.locateOnScreen(item.image))

    exchange.set_price(price)

    exchange.set_amount(amount)

    exchange.confirm()

    return orders.Order(slot, item)
