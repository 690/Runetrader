from tools import item_database


class Item:
    """ Basic class for storing an item """

    def __init__(self, item_name):
        name = item_name
        itemID = item_database.item_name_to_id(name)
        #image = item_database.get_item_image(itemID)
