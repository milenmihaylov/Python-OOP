from creational.utils import StrDictMixin


# python singleton
# create decorator
def singleton(cls):
    instances = []  # use list, not nonlocal

    def wrapper(*args, **kwargs):
        if not instances:
            instances.append(cls(*args, **kwargs))
        return instances[0]

    return wrapper


@singleton
class House(StrDictMixin):
    def __init__(self, floors_count, has_pool):
        self.floors_count = floors_count
        self.has_pool = has_pool


class HousePureSingleton(StrDictMixin):
    _instance = None

    def __init__(self, floors_count, has_pool):
        self.floors_count = floors_count
        self.has_pool = has_pool
        HousePureSingleton._instance = self

    @classmethod
    def instance(cls):
        return cls._instance


print(House(2, True))
print(House(3, False))
print(House(1, True) == House(3, False))


# Practical singleton
class HouseFactory:
    _house_instance = House(3, False)

    def get_house(self):
        return self._house_instance
