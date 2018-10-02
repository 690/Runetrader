import datetime


class Order:
    """ Basic class for storing information about an order """

    def __init__(self, slot, item):
        self.slot = slot
        self.item = item

        self.last_datetime = datetime.datetime.now()
