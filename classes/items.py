from tools import item_database


class item:
    """ Basic class for storing an item """

    def __init__(self, item_name, amount=1):
        self.item_name = item_name
        self.itemID = item_database.item_name_to_id(self.item_name)
        self.item_image_name = item_database.get_item_image(self.itemID)
        self.amount = amount
