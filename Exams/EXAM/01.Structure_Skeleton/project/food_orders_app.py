from typing import List

from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    __valid_meals = ("Starter", "MainDish", "Dessert")
    __receipt_id = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")
        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.__valid_meals:
                self.menu.append(meal)

    def __check_ready_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def show_menu(self):
        self.__check_ready_menu()
        menu_list = []
        for meal in self.menu:
            menu_list.append(meal.details())
        return '\n'.join(menu_list)

    def __select_client(self, phone: str):
        for client in self.clients_list:
            if client.phone_number == phone:
                return client
        return self.register_client(phone)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.__check_ready_menu()
        current_client = self.__select_client(client_phone_number)
        current_order = []
        current_bill = 0
        for meal_name, quantity in meal_names_and_quantities.items():
            in_the_menu = False
            for meal in self.menu:
                if meal_name == meal.name:
                    in_the_menu = True
                    if quantity <= meal.quantity:
                        current_order.append(meal)
                        current_bill += meal.price * quantity
                    else:
                        raise Exception(f"Not enough quantity of {meal.__class__.name}: {meal_name}!")
            if not in_the_menu:
                raise Exception(f"{meal_name} is not on the menu!")

        current_client.shopping_cart.extend(current_order)
        current_client.bill += current_bill
        for meal_name, quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal_name == meal.name:
                    meal.quantity -= quantity

        total_ordered_meals_names = []
        for meal in current_client.shopping_cart:
            total_ordered_meals_names.append(meal.name)
        return f"Client {client_phone_number} successfully ordered {', '.join(total_ordered_meals_names)} " \
               f"for {current_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                if not client.shopping_cart:
                    raise Exception("There are no ordered meals!")

                for item in client.shopping_cart:
                    for meal in self.menu:
                        if meal.name == item.name:
                            meal.quantity += item.quantity

                client.shopping_cart = []
                client.bill = 0
                return f"Client {client_phone_number} successfully canceled his order."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def finish_order(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                if not client.shopping_cart:
                    raise Exception("There are no ordered meals!")
                total_paid_money = client.bill
                client.bill = 0
                self.__receipt_id += 1
                client.shopping_cart.clear()

                return f"Receipt #{self.__receipt_id} with total amount of {total_paid_money:.2f} " \
                       f"was successfully paid for {client_phone_number}."
