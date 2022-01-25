from car_manager import Car

import unittest


def normal_car():
    make = 'VW'
    model = 'Golf'
    fuel_consumption = 6
    fuel_capacity = 50
    return Car(make, model, fuel_consumption, fuel_capacity)


class CarTests(unittest.TestCase):
    make = 'VW'
    model = 'Golf'
    fuel_consumption = 6
    fuel_capacity = 50

    def test_init_make__expect_valid(self):
        car = normal_car()

        self.assertEqual(self.make, car.make)
        self.assertEqual(self.model, car.model)
        self.assertEqual(self.fuel_consumption, car.fuel_consumption)
        self.assertEqual(self.fuel_capacity, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_init__when_make_is_none__expect_exception(self):
        make = None
        model = 'Golf'
        fuel_consumption = 6
        fuel_capacity = 50
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)

        self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test_init__when_make_is_empty_str__expect_exception(self):
        make = ''
        model = 'Golf'
        fuel_consumption = 6
        fuel_capacity = 50
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)

        self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test_init__when_model_is_none__expect_exception(self):
        make = 'VW'
        model = None
        fuel_consumption = 6
        fuel_capacity = 50
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)

        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test_init__when_model_is_empty_str__expect_exception(self):
        make = 'VW'
        model = ''
        fuel_consumption = 6
        fuel_capacity = 50
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)

        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test_fuel_consumption__when_0__expect_exception(self):
        make = 'VW'
        model = 'Golf'
        fuel_consumption = 0
        fuel_capacity = 50
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_fuel_consumption__when_negative__expect_exception(self):
        make = 'VW'
        model = 'Golf'
        fuel_consumption = -1
        fuel_capacity = 50
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_fuel_capacity__when_0__expect_exception(self):
        make = 'VW'
        model = 'Golf'
        fuel_consumption = 6
        fuel_capacity = 0
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_fuel_capacity__when_negative__expect_exception(self):
        make = 'VW'
        model = 'Golf'
        fuel_consumption = 6
        fuel_capacity = -1
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_fuel_amount__when_negative__expect_exception(self):
        car = normal_car()
        with self.assertRaises(Exception) as context:
            car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(context.exception))

    def test_refuel__with_0_fuel__expect_exception(self):
        car = normal_car()
        with self.assertRaises(Exception) as context:
            car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_refuel__with_negative_fuel__expect_exception(self):
        car = normal_car()
        with self.assertRaises(Exception) as context:
            car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_refuel__with_positive_fuel__expect_fuel_amount_increase(self):
        make = 'VW'
        model = 'Golf'
        fuel_consumption = 6
        fuel_capacity = 50
        car = Car(make, model, fuel_consumption, fuel_capacity)

        car.refuel(1)
        self.assertEqual(1, car.fuel_amount)

    def test_drive__when_fuel_is_0__expect_exception(self):
        make = 'VW'
        model = 'Golf'
        fuel_consumption = 1
        fuel_capacity = 10
        car = Car(make, model, fuel_consumption, fuel_capacity)

        with self.assertRaises(Exception) as context:
            car.drive(1)

        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))

    def test_drive__when_fuel_is_1_and_valid_distance__expect_valid(self):
        make = 'VW'
        model = 'Golf'
        fuel_consumption = 1
        fuel_capacity = 10
        car = Car(make, model, fuel_consumption, fuel_capacity)

        car.refuel(1)
        car.drive(100)

        self.assertEqual(0.0, car.fuel_amount)


if __name__ == '__main__':
    unittest.main()
