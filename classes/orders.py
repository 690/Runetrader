import window
from classes import items, inventory as inventory
import datetime


class order:
    """ Parent class of orders """

    def __init__(self, item, amount, ppi):
        self.item = item
        self.amount = amount
        self.ppi = ppi  # Price per item

        self.last_margin_check = datetime.datetime.now()
        self.min_margin = analysis.min_margin(self.item.itemID, self.ppi)

    @property
    def has_completed(self):
        pass

    def abort(self):
        pass

    def update(self):
        if self.has_completed:
            self.retrieve_item()
            return True

        if self.last_margin_check < datetime.datetime.now() - datetime.timedelta(hours=1):
            margin = analysis.find_margin(self.item.itemID)
            self.last_margin_check = datetime.datetime.now()

            if margin['sell'] < self.ppi + self.min_margin:
                self.abort()



def buy_order(order):

    def retrieve_item(self):
        window.retrieve_(self.item.itemID)

        inventory.add(self.item.itemID, self.amount)

    def update(self):
        if self.has_completed:
            self.retrieve_item()
            return True


def sell_order(order):
    def retrieve_item(self):
        window.retrieve(self.item.itemID)

        inventory.my_inventory.add(items.item('coins', self.ppi * self.amount))
