from creational.house import House


# factory method
class HouseFactory:
    @staticmethod
    def get_no_pool_house(floors_count, has_garage, rooms_count, balconies_count, town):
        return House(floors_count, has_garage, True, rooms_count, balconies_count, town, False)


