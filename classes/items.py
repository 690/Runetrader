from tools import item_database


class Item:
    """ Basic class for storing an item """

    def __init__(self, item_name, amount=1):
        self.name = item_name
        self.itemID = item_database.item_name_to_id(self.name)
        self.image = item_database.get_item_image(self.itemID)

        self.amount = amount
