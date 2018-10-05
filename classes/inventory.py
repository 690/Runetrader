class Slot:

    def __init__(self, coordinates, item, amount):
        self.coordinates = coordinates
        self.item = item
        self.amount = amount

    def set(self, i, a):
        self.item = i
        self.amount = a


class Inventory:

    def __init__(self, coordinates):

        self.coordinates = coordinates
        self.inventory_list = []

        # Initialize 2D matrix of Slot objects for inventory

        rows, cols = 7, 4
        x0, y0, w, h = self.coordinates

        for x in range(rows):
            for y in range(cols):
                nz = round(w / cols)
                nw = round(h / rows)
                nx = (x0 + nz * y)
                ny = (y0 + nw * x)

                crop = round(nw/3)
                self.inventory_list.append(Slot((nx+crop, ny+crop, nz-crop, nw-crop), None, 0))


    @property
    def coins(self):
        return self.inventory_list[0].amount

    def find(self, item):
        """ returns the Slot object containing the item """
        for i, j in enumerate(self.inventory_list):
            if self.inventory_list[i].item.itemID == item.itemID:
                return self.inventory_list[i]
            return None

    def add(self, item, amount):
        """ Looks for an open spot in the inventory and adds the given item,
         if item already exists, it adds the given amount """

        for slot in self.inventory_list:
            if slot.item is None:
                slot.item = item
                slot.amount = amount

    def remove(self, item, amount):
        """ Removes a certain amount of a given itemID from the inventory list,
         if all are removed it deletes the entire entry """

        for slot in self.inventory_list:
            if slot.item.itemID == item.itemID:
                if amount > slot.amount:
                    slot.item = None
                    slot.amount = 0
                else:
                    slot.amount -= amount
