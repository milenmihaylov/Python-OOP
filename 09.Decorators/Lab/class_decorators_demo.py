import functools
from dataclasses import dataclass


def singleton(cls):
    instances = []

    @functools.wraps
    def wrapper(*args, **kwargs):
        if not instances:
            instances.append(cls(*args, **kwargs))
        return instances[0]

    return wrapper


@singleton
@dataclass
class Person:
    name: str
    age: int


p1 = Person('Gosho', 19)
p2 = Person('Pesho', 29)
p3 = Person('Tony', 39)
print(p1)
print(p2)
print(p3)
