from creational.house import House


class HouseBuilder:
    _rooms_count = 0
    _floors_count = 0
    _has_garage = False
    _has_electricity = False
    _balconies_count = 0
    _town = 'Unknown'
    _has_pool = False

    def with_rooms_count(self, rooms_count):
        self._rooms_count = rooms_count

    def with_floors_count(self, floors_count):
        self._floors_count = floors_count

    def with_garage(self):
        self._has_garage = True

    def with_electricity(self):
        self._has_electricity = True

    def with_balconies_count(self, balconies_count):
        self._balconies_count = balconies_count

    def with_town(self, town):
        self._town = town

    def with_pool(self):
        self._has_pool = True

    def build(self):
        return House(self._floors_count,
                     self._has_garage,
                     self._has_electricity,
                     self._rooms_count,
                     self._balconies_count,
                     self._town,
                     self._has_pool)


house_builder = HouseBuilder()
house_builder.with_town('Sofia')
house_builder.with_electricity()
house_builder.with_floors_count(3)
house_builder.with_rooms_count(2)
my_house = house_builder.build()

print(my_house)


# Instead of typing the methods every time, you can use a Factory with the Builder
# Factory + Builder:
class HouseFactory:
    @staticmethod
    def get_house_in_burgas(floors_count, rooms_count, balconies_count):
        builder = HouseBuilder()
        builder.with_town('Burgas')
        builder.with_floors_count(floors_count)
        builder.with_rooms_count(rooms_count)
        builder.with_balconies_count(balconies_count)
        return builder.build()


# Factories are abstractions over constructor (__init__)
# Builder s are abstractions over factories
