from typing import List


class Animal:
    _sound = None
    _species = None

    def get_sound(self):
        return self._sound

    def get_species(self):
        return self._species


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.get_sound())


class Dog(Animal):
    _sound = 'bau-bau'
    _species = 'dog'


class Cat(Animal):
    _sound = 'meow-meow'
    _species = 'cat'


animals = [Dog(), Cat()]
animal_sound(animals)
