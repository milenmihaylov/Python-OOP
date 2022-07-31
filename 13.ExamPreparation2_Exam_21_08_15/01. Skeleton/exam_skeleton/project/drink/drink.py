from abc import ABC, abstractmethod

from project.utils import is_positive


class Drink(ABC):

    __INVALID_NAME_MSG = 'Name cannot be empty string or white space!'
    __INVALID_PORTION_MSG = 'Portion cannot be less than or equal to zero!'
    __INVALID_BRAND_MSG = 'Brand cannot be empty string or white space!'

    @abstractmethod  # BAD PRACTICE
    def __init__(self, name: str, portion: int, price: float, brand: str):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @classmethod
    def __validate_name(cls, value: str):
        if not value or not value.strip():
            raise ValueError(cls.__INVALID_NAME_MSG)

    @classmethod
    def __validate_portion(cls, value):
        if not is_positive(value):
            raise ValueError(cls.__INVALID_PORTION_MSG)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        self.__validate_portion(value)
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if not self.__is_valid_string(value):
            raise ValueError(self.__INVALID_BRAND_MSG)
        self.__brand = value

    @staticmethod
    def __is_valid_string(text: str):
        if not text or not text.strip():
            return False
        return True

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
