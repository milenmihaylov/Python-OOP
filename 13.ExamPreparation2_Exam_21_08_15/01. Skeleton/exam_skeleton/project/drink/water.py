from project.drink.drink import Drink


class Water(Drink):

    __WATER_PRICE = 1.5  # lv

    def __init__(self, name: str, portion: int, brand: str):
        super().__init__(name, portion, self.__WATER_PRICE, brand)

