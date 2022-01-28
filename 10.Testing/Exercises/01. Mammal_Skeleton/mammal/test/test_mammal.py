from project.mammal import Mammal

import unittest


class MammalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.name = 'Sharo'
        self.mammal_type = 'dog'
        self.sound = 'Bau-bau'
        self.dog = Mammal(self.name, self.mammal_type, self.sound)

    def test_init__expect_valid(self):
        self.assertEqual(self.name, self.dog.name)
        self.assertEqual(self.mammal_type, self.dog.type)
        self.assertEqual(self.sound, self.dog.sound)

    def test_get_kingdom__expect_valid(self):
        self.assertEqual(self.dog._Mammal__kingdom, self.dog.get_kingdom())

    def test_make_sound__expect_valid(self):
        self.assertEqual(f"{self.name} makes {self.sound}", self.dog.make_sound())

    def test_info__expect_valid(self):
        self.assertEqual(f"{self.name} is of type {self.mammal_type}", self.dog.info())


if __name__ == '__main__':
    unittest.main()
