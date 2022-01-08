from typing import List


class Animal:
    def __init__(self, species, sound):
        self.sound = sound
        self.species = species


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.sound)


dog = Animal('dog', 'bau-bau')
animals = [dog, Animal('cat', 'meow'), Animal('chicken', 'chick-chick')]

animal_sound(animals)
