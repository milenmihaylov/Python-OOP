from typing import List

from project.meals.meal import Meal


class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: List[Meal] = []
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        if not (value[0] == '0' and len(value) == 10 and value.isnumeric()):
            raise ValueError("Invalid phone number!")
        self.__phone_number = value
