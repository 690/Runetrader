import window


class slot():

    def __init__(self, coordinates):
        self.coordinates = coordinates

        self.buy_button = window.get_buy_slot(self.coordinates)
        self.sell_button = window.get_sell_slot(self.coordinates)
