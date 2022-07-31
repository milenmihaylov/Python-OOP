from abc import ABC, abstractmethod

from project.utils import is_positive


class BakedFood(ABC):

    __INVALID_NAME_MSG = 'Name cannot be empty string or white space!'
    __INVALID_PRICE_MSG = 'Price cannot be less than or equal to zero!'

    @abstractmethod  # BAD PRACTICE
    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion  # g
        self.price = price  # lv

    @classmethod
    def __validate_name(cls, value: str):
        if not value or not value.strip():
            raise ValueError(cls.__INVALID_NAME_MSG)

    @classmethod
    def __validate_price(cls, value: float):
        if not is_positive(value):
            raise ValueError(cls.__INVALID_PRICE_MSG)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__validate_price(value)
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
