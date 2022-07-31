from abc import ABC, abstractmethod
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.utils import is_positive


class Table(ABC):

    __MIN_TABLE_NUMBER = None
    __MAX_TABLE_NUMBER = None
    __INVALID_TABLE_NUMBER_MSG = None
    __INVALID_CAPACITY_MSG = 'Capacity has to be greater than 0!'

    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @classmethod
    def __validate_table_number(cls, value):
        if cls.__MIN_TABLE_NUMBER and value < cls.__MIN_TABLE_NUMBER:
            raise ValueError(cls.__INVALID_TABLE_NUMBER_MSG)
        if cls.__MAX_TABLE_NUMBER and value > cls.__MAX_TABLE_NUMBER:
            raise ValueError(cls.__INVALID_TABLE_NUMBER_MSG)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        self.__validate_table_number(value)
        self.__table_number = value

    @classmethod
    def __validate_capacity(cls, value):
        if not is_positive(value):
            raise ValueError(cls.__INVALID_CAPACITY_MSG)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__validate_capacity(value)
        self.__capacity = value

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        bill = 0
        for food in self.food_orders:
            bill += food.price
        for drink in self.drink_orders:
            bill += drink.price
        return bill

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" \
                   f"Type: {self.__class__.__name__}\n" \
                   f"Capacity: {self.capacity}"
