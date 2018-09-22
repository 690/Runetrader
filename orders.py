import window
import inventory as inventory
import item_database


class order:
    """ Parent class of orders """

    def __init__(self, itemID, amount, ppi):
        self.id = itemID
        self.amount = amount
        self.ppi = ppi  # Price per item

    @property
    def has_completed(self):
        return window.check_slot(self.slot)

    def update(self):
        if self.has_completed:
            self.retrieve_item()


def buy_order(order):
    def retrieve_item(self):
        window.retrieve_(self.itemID)

        inventory.add(self.itemID, self.amount)


def sell_order(order):
    def retrieve_item(self):
        window.retrieve(self.itemID)

        inventory.add(item_database.item_name_to_id("coins"), self.ppi * self.amount)