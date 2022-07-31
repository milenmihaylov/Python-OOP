from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class FoodFactory:
    @staticmethod
    def create(food_type: str, name: str, price: float):
        if food_type == "Bread":
            return Bread(name, price)
        elif food_type == "Cake":
            return Cake(name, price)
        else:
            return None


class DrinkFactory:
    @staticmethod
    def create(drink_type: str, name: str, portion: int, brand: str):
        if drink_type == "Tea":
            return Tea(name, portion, brand)
        elif drink_type == "Water":
            return Water(name, portion, brand)
        else:
            return None


class TableFactory:
    @staticmethod
    def create(table_type: str, table_number: int, capacity: int):
        if table_type == 'InsideTable':
            return InsideTable(table_number, capacity)
        elif table_type == 'OutsideTable':
            return OutsideTable(table_number, capacity)
        else:
            return None


class Bakery:

    __INVALID_NAME_MSG = 'Name cannot be empty string or white space!'

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0
        self.__food_names = set()
        self.__drink_names = set()
        self.__table_nums = set()

    @classmethod
    def __validate_name(cls, text: str):
        if not text or not text.strip():
            raise ValueError(cls.__INVALID_NAME_MSG)
        return True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    def __valid_food(self, food_type: str, name: str):
        if name in self.__food_names:
            raise Exception(f'Added {name} ({food_type}) to the food menu')

    def add_food(self, food_type: str, name: str, price: float):
        self.__valid_food(food_type, name)
        food = FoodFactory().create(food_type, name, price)
        self.food_menu.append(food)
        self.__food_names.add(food.name)
        return f'Added {name} ({food_type}) to the food menu'

    def __valid_drink(self, drink_type: str, name: str):
        if name in self.__drink_names:
            raise Exception(f'{drink_type} {name} is already in the menu!')

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        self.__valid_drink(drink_type, name)
        drink = DrinkFactory().create(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)
        self.__drink_names.add(drink.name)
        return f"Added {name} ({brand}) to the drink menu"

    def __valid_table(self, table_num: int):
        if table_num in self.__table_nums:
            raise Exception(f"Table {table_num} is already in the bakery!")

    def add_table(self, table_type: str, table_number: int, capacity: int):
        self.__valid_table(table_number)
        table = TableFactory().create(table_type, table_number, capacity)
        self.tables_repository.append(table)
        self.__table_nums.add(table_number)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def __get_table_by_number(self, table_number):
        tables = [t for t in self.tables_repository if t.table_number == table_number]
        if tables:
            return tables[0] if tables else None

    def order_food(self, table_number: int, *food_names: str):
        not_in_menu = []
        table = self.__get_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"
        for food_name in food_names:
            food_menu_list = [food.name for food in self.food_menu]
            if food_name in food_menu_list:
                i = food_menu_list.index(food_name)
                table.order_food(self.food_menu[i])
            else:
                not_in_menu.append(food_name)
        return self.__return_order_food(table, not_in_menu)

    def __return_order_food(self, table: Table, not_in_menu: list):
        ordered_food_str = f"Table {table.table_number} ordered:"
        not_in_menu_str = ''
        for food in table.food_orders:
            ordered_food_str += f"\n - {food.name}: {food.portion}g - {food.price}lv"
        if not_in_menu:
            not_in_menu_str = f'{self.name} does not have in the menu:\n'
            not_in_menu_str += '\n'.join(not_in_menu)
        return ordered_food_str + not_in_menu_str

    def order_drink(self, table_number: int, *drinks_names: str):
        not_in_menu = []
        for table in self.tables_repository:
            if table.table_number == table_number:
                for drink_name in drinks_names:
                    drink_menu_list = [drink.name for drink in self.drinks_menu]
                    if drink_name in drink_menu_list:
                        i = drink_menu_list.index(drink_name)
                        table.order_drink(self.drinks_menu[i])
                    else:
                        not_in_menu.append(drink_name)
                return self.__return_order_drink(table, not_in_menu)
        return f"Could not find table {table_number}"

    def __return_order_drink(self, table: Table, not_in_menu: list):
        ordered_drink_str = f"Table {table.table_number} ordered:"
        not_in_menu_str = ''
        for drink in table.drink_orders:
            ordered_drink_str += f"\n - {drink.name} {drink.brand} - {drink.portion}ml - {drink.price}lv"
        if not_in_menu:
            not_in_menu_str = f'{self.name} does not have in the menu:\n'
            not_in_menu_str += '\n'.join(not_in_menu)
        return ordered_drink_str + not_in_menu_str

    def leave_table(self, table_number: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                bill = table.get_bill()
                self.total_income += bill
                table.clear()
                return f"Table: {table_number}\n" \
                       f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        result = [table.free_table_info() for table in self.tables_repository if not table.is_reserved]
        return '\n'.join(result)

    def get_total_income(self):
        return f"{self.total_income:.2f}"
