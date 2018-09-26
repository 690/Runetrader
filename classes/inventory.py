
import pickle
from classes import items
from tools import item_database
import pyautogui


class inventory:

    def __init__(self, coin_capital):

        self.inventory_list = [0 for x in range(0, 28)]
        self.inventory_list[0] = items.item('coins', coin_capital)
        self.save_inventory()

    def load_inventory(self):
        """ loads inventory.pickle into the current inventory_list, replacing the old one."""

        with open('../data/inventory.pickle', 'rb') as f:
            self.inventory_list = pickle.load(f)

    def save_inventory(self):
        """ Writes the current inventory to inventory.pickle """

        with open('../data/inventory.pickle ', 'wb') as f:
            pickle.dump(self.inventory_list, f)

    def add(self, item):
        """ Looks for an open spot in the inventory and adds the given item,
         if item already exists, it adds the given amount """

        for i, j in enumerate(self.inventory_list):
            try:
                self.inventory_list[i].itemID == item.itemID
                self.inventory_list[i].amount += item.amount
                return
            except AttributeError as e:
                pass

        for i, j in enumerate(self.inventory_list):
            if self.inventory_list[i] == 0:
                self.inventory_list[i] = items.item(item_database.item_id_to_name(item.itemID))
                return

        raise IndexError("No available inventory slots")

    def remove(self, item):
        """ Removes a certain amount of a given itemID from the inventory list,
         if all are removed it deletes the entire entry """

        for i, j in enumerate(self.inventory_list):
            if self.inventory_list[i].itemID == item.itemID:
                if item.amount == self.inventory_list[i].amount:
                    self.inventory_list[i] = 0
                else:
                    self.inventory_list[i].amount -= int(item.amount)

                self.save_inventory()
                return None

        raise IndexError("No item with id '{0}' in inventory".format(item.itemID))


def setup(coin_capital):
    my_inventory = inventory(coin_capital)
