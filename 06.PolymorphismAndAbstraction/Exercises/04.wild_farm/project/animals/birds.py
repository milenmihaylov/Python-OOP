from project.animals.animal import Bird
from project.food import Food, Meat


class Owl(Bird):

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.25 * food.quantity
        self.food_eaten += food.quantity

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def feed(self, food: Food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity

    def make_sound(self):
        return "Cluck"
