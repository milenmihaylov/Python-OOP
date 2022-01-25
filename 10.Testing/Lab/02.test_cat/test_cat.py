from cat import Cat

import unittest


class CatTests(unittest.TestCase):
    name = 'Tom'

    def setUp(self) -> None:
        print('---setup---')
        self.cat = Cat(self.name)

    def test_eat__expect_size_increase_by_1(self):
        expected_size = 0 + 1

        self.cat.eat()
        actual_size = self.cat.size

        self.assertEqual(expected_size, actual_size)

    def test_eat__expect_fed_to_be_true(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_eat__when_fed_is_true__expect_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as context:
            self.cat.eat()

        self.assertEqual('Already fed.', str(context.exception))

    def test_sleep_when_fed_is_false__expect_exception(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as context:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(context.exception))

    def test_sleepy_after_sleep__expect_false(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
