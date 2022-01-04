from project.animals.animal import Mammal
from project.food import Food, Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def feed(self, food: Food):
        if not (isinstance(food, Vegetable) or isinstance(food, Fruit)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.10 * food.quantity
        self.food_eaten += food.quantity

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.40 * food.quantity
        self.food_eaten += food.quantity

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def feed(self, food: Food):
        if not (isinstance(food, Vegetable) or isinstance(food, Meat)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.10 * food.quantity
        self.food_eaten += food.quantity

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 1.00 * food.quantity
        self.food_eaten += food.quantity

    def make_sound(self):
        return "ROAR!!!"
