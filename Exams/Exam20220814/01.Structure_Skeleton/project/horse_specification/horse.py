from abc import ABC, abstractmethod


class Horse(ABC):
    _MAX_SPEED = None
    _TRAIN_SPEED_INCREASE = None

    @abstractmethod
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self._MAX_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    def train(self):
        if (self.speed + self._TRAIN_SPEED_INCREASE) >= self._MAX_SPEED:
            self.speed = self._MAX_SPEED
        else:
            self.speed += self._TRAIN_SPEED_INCREASE

