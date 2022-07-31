from creational.utils import StrDictMixin


class House(StrDictMixin):
    def __init__(self, floors_count, has_garage, has_electricity, rooms_count, balconies_count, town, has_pool):
        self.floors_count = floors_count
        self.has_garage = has_garage
        self.has_electricity = has_electricity
        self.rooms_count = rooms_count
        self.balconies_count = balconies_count
        if not town:
            town = "Sofia"
        self.town = town
        self.has_pool = has_pool

    @classmethod
    def get_house_in_sofia(cls, floors_count, has_garage,  rooms_count, balconies_count):
        return cls(floors_count, has_garage, True, rooms_count, balconies_count, 'Sofia', False)
