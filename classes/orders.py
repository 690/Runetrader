import datetime


class Order:
    """ Basic class for storing information about an order """

    def __init__(self, slot, item, amount=1, ppi=None):
        self.slot = slot
        self.item = item
        self.amount = amount
        self.ppi = ppi  # Price per item

        self.last_margin_check = datetime.datetime.now()
