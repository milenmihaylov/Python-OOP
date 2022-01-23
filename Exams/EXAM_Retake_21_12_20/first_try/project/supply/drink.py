from supply.supply import Supply


class Drink(Supply):
    def __init__(self, name=None, energy=15):
        super().__init__(name, energy)
