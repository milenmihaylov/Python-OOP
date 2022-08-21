from typing import List

from project.car.car import Car

from project.driver import Driver

from project.race import Race

from project.car.muscle_car import MuscleCar

from project.car.sports_car import SportsCar


class Controller:
    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        # Check if a car of the same model exists
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        # Create car and append
        if car_type == 'MuscleCar':
            self.cars.append(MuscleCar(model, speed_limit))
            return f"{car_type} {model} is created."
        elif car_type == 'SportsCar':
            self.cars.append(SportsCar(model, speed_limit))
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def _check_valid_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        raise Exception(f"Driver {driver_name} could not be found!")

    def _check_valid_car(self, car_type):
        length = len(self.cars)
        for i in range(length - 1, -1, -1):
            car = self.cars[i]
            if self.cars[i].__class__.__name__ == car_type and not car.is_taken:
                return i
        raise Exception(f"Car {car_type} could not be found!")

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self._check_valid_driver(driver_name)
        car_index = self._check_valid_car(car_type)
        if driver.car:
            old_model = driver.car.model
            for car in self.cars:
                if car.model == old_model:
                    car.is_taken = False
            driver.car = self.cars[car_index]
            self.cars[car_index].is_taken = True
            return f"Driver {driver.name} changed his car from {old_model} to {driver.car.model}."

        driver.car = self.cars[car_index]
        self.cars[car_index].is_taken = True
        return f"Driver {driver_name} chose the car {driver.car.model}."

    def _check_valid_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        raise Exception(f"Race {race_name} could not be found!")

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self._check_valid_race(race_name)
        driver = self._check_valid_driver(driver_name)
        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    @staticmethod
    def _format_return(drivers, race_name):
        ll = []
        for i in range(3):
            ll.append(
                f"Driver {drivers[i].name} wins the {race_name} race with a speed of {drivers[i].car.speed_limit}.")
        return '\n'.join(ll)

    def start_race(self, race_name: str):
        race = self._check_valid_race(race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        winning_order = sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True)
        for i in range(3):
            winning_order[i].number_of_wins += 1
        return self._format_return(winning_order, race.name)
