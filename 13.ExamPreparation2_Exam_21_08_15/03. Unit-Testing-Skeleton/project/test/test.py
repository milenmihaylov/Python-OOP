import unittest

from project.pet_shop import PetShop


class TestPetShop(unittest.TestCase):
    def setUp(self):
        self.name_shop = 'ZooShop'
        self.p_shop = PetShop(self.name_shop)
        self.food_name = 'test_food'
        self.pet_name = 'Sharo'

    def test_init(self):
        self.assertEqual('ZooShop', self.p_shop.name)
        self.assertEqual([], self.p_shop.pets)
        self.assertEqual({}, self.p_shop.food)

    def test_add_food_bad_weather(self):

        with self.assertRaises(ValueError) as context:
            self.p_shop.add_food(self.food_name, 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_add_food(self):
        quantity = 1
        result = self.p_shop.add_food(self.food_name, quantity)
        self.assertTrue(self.food_name in self.p_shop.food)
        self.assertEqual(f"Successfully added {quantity:.2f} grams of {self.food_name}.", result)

        self.p_shop.add_food(self.food_name, 2)
        self.assertEqual(self.p_shop.food[self.food_name], 3)

    def test_add_pet(self):
        result = self.p_shop.add_pet(self.pet_name)
        self.assertTrue(self.pet_name in self.p_shop.pets)
        self.assertEqual(f"Successfully added {self.pet_name}.", result)

    def test_add_pet_bad_weather(self):
        self.p_shop.add_pet(self.pet_name)
        with self.assertRaises(Exception) as context:
            self.p_shop.add_pet(self.pet_name)
        self.assertEqual("Cannot add a pet with the same name", str(context.exception))

    def test_feed_pet_invalid_food(self):
        self.p_shop.add_pet(self.pet_name)
        result = self.p_shop.feed_pet(self.food_name, self.pet_name)
        self.assertEqual(f'You do not have {self.food_name}', result)

    def test_feed_pet_invalid_pet_name(self):
        self.p_shop.add_food(self.food_name, 1)
        with self.assertRaises(Exception) as context:
            self.p_shop.feed_pet(self.food_name, self.pet_name)
        self.assertEqual(f"Please insert a valid pet name", str(context.exception))

    def test_feed_pet_add_food(self):
        self.p_shop.add_food(self.food_name, 1)
        self.p_shop.add_pet(self.pet_name)
        result = self.p_shop.feed_pet(self.food_name, self.pet_name)
        self.assertEqual("Adding food...", result)
        self.assertEqual(1001.00, self.p_shop.food[self.food_name])

    def test_feed_pet(self):
        self.p_shop.add_food(self.food_name, 100)
        self.p_shop.add_pet(self.pet_name)
        result = self.p_shop.feed_pet(self.food_name, self.pet_name)
        self.assertEqual(f"{self.pet_name} was successfully fed", result)
        self.assertEqual(0, self.p_shop.food[self.food_name])

    def test_repr(self):
        self.p_shop.add_pet(self.pet_name)
        self.p_shop.add_pet('Lucky')

        expected = f'Shop {self.p_shop.name}:\n' \
               f'Pets: {", ".join([self.pet_name, "Lucky"])}'

        self.assertEqual(expected, self.p_shop.__repr__())


if __name__ == '__main':
    unittest.main()
