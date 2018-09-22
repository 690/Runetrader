import image_handler
import pickle

inventory_list = []


def load_inventory():
    """ loads inventory.pickle into the current inventory_list, replacing the old one."""
    with open('inventory.pickle', 'rb') as f:
        inventory_list = pickle.load(f)


def save_inventory():
    """ Writes the current inventory to inventory.pickle """
    with open('inventory.pickle ', 'wb') as f:
        pickle.dump(inventory_list, f)


def add(itemID, amount):
    """ Looks for an open spot in the inventory and adds the given item,
     if item already exists, it adds the given amount """

    for i, j in enumerate(inventory_list):
        try:
            inventory_list[i].keys() == itemID
            inventory_list[i][itemID] += amount
            return
        except AttributeError as e:
            pass

    for i, j in enumerate(inventory_list):
        if inventory_list[i] == 0:
            inventory_list[i] = {itemID : amount}
            return

    raise IndexError("No available inventory slots")


def remove(itemID, amount):
    """ Removes a certain amount of a given itemID from the inventory list,
     if all are removed it deletes the entire entry """

    for i, j in enumerate(inventory_list):
        if inventory_list[i].keys() == itemID:
            if amount == inventory_list[i][itemID]:
                inventory_list[i] = 0
                image_handler.remove(itemID)
            else:
                inventory_list[i][itemID] -= int(amount)

            save_inventory()
            return None

    raise IndexError("No item with id '{0}' in inventory".format(itemID))


def setup(coin_capital):
    """ Initialize inventory - do this on startup """

    inventory_list = [0 for x in range(0, 28)]
    inventory_list[0] = {"Coins": coin_capital}
    save_inventory()

