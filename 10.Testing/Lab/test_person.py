import unittest
from unittest import TestCase

from person import Person


class TestPerson(TestCase):
    def test_get_full_name__when_valid_names_and_age__expect_valid(self):
        # arrange
        first_name = 'Test'
        second_name = 'Person'
        age = 19
        person = Person(first_name, second_name, age)

        # act
        actual_full_name = person.get_full_name()

        # assert
        expected_full_name = f'{first_name} {second_name}'
        self.assertEqual(expected_full_name, actual_full_name)

    def test_get_info__when_valid_names_and_age__expect_valid(self):
        # arrange
        first_name = 'Test'
        last_name = 'Person'
        age = 19
        person = Person(first_name, last_name, age)

        # act
        actual_get_info = person.get_info()

        # assert
        expected_get_full_name = f"{first_name} {last_name} is {age} yeats old."
        self.assertEqual(actual_get_info, expected_get_full_name)

    def setUp(self) -> None:
        pass

    def setUpClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
