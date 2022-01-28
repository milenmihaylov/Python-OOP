from project.vehicle import Vehicle

import unittest


class VehicleTests(unittest.TestCase):

    def test_init__expect_valid(self):
        fuel = 100.0
        horse_power = 450.5
        vehicle = Vehicle(fuel, horse_power)

        self.assertEqual(fuel, vehicle.fuel)
        self.assertEqual(horse_power, vehicle.horse_power)
        self.assertEqual(vehicle.fuel, vehicle.capacity)
        self.assertEqual(vehicle.DEFAULT_FUEL_CONSUMPTION, vehicle.fuel_consumption)
        self.assertEqual(float, type(vehicle.DEFAULT_FUEL_CONSUMPTION))

    def test_drive__when_fuel_is_less_than_fuel_needed__expect_exception(self):
        fuel = 9.9
        horse_power = 450.5
        vehicle = Vehicle(fuel, horse_power)
        vehicle.fuel_consumption = 10

        # fuel_needed = vehicle.fuel_consumption * kilometers = 10 * 1 = 10
        with self.assertRaises(Exception) as context:
            vehicle.drive(1)

        self.assertEqual("Not enough fuel", str(context.exception))

    def test_drive__when_fuel_is_equal_to_fuel_needed__expect_valid(self):
        fuel = 10
        horse_power = 450.5
        vehicle = Vehicle(fuel, horse_power)
        vehicle.fuel_consumption = 10
        vehicle.drive(1)

        self.assertEqual(0, vehicle.fuel)

    def test_refuel__when_added_fuel_is_more_than_capacity__expect_exception(self):
        fuel = 8
        horse_power = 450.5
        vehicle = Vehicle(fuel, horse_power)
        vehicle.capacity = 10

        with self.assertRaises(Exception) as context:
            vehicle.refuel(3)

        self.assertEqual("Too much fuel", str(context.exception))

    def test_refuel__when_added_fuel_is_equal_to_capacity__expect_valid(self):
        fuel = 8
        horse_power = 450.5
        vehicle = Vehicle(fuel, horse_power)
        vehicle.capacity = 10

        vehicle.refuel(2)

        self.assertEqual(10, vehicle.fuel)

    def test_str__expect_valid(self):
        fuel = 8
        horse_power = 450.5
        vehicle = Vehicle(fuel, horse_power)
        expect = f"The vehicle has {horse_power} " \
                 f"horse power with {fuel} fuel left and {vehicle.DEFAULT_FUEL_CONSUMPTION} fuel consumption"

        self.assertEqual(expect, str(vehicle))


if __name__ == '__main__':
    unittest.main()
