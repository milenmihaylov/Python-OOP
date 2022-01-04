from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


class Car(Vehicle):
    __fuel_consumption_increase = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        required_fuel = distance * (self.fuel_consumption + self.__fuel_consumption_increase)
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    __fuel_consumption_increase = 1.6
    __fuel_loss = 0.05

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption )

    def drive(self, distance):
        required_fuel = distance * (self.fuel_consumption + self.__fuel_consumption_increase)
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * (1 - self.__fuel_loss)


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
