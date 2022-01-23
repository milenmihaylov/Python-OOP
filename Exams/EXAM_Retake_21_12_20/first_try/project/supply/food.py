from supply.supply import Supply


class Food(Supply):
    def __init__(self, name=None, energy=25):
        super().__init__(name, energy)
