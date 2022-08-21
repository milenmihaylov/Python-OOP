from project.car.car import Car


class Driver:
    def __init__(self, name: str, car: Car = None, number_of_wins: int = 0):
        self.name = name
        self.car: Car = car
        self.number_of_wins = number_of_wins
