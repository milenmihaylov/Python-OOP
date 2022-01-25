from extended_list import IntegerList

import unittest


class IntegerListTests(unittest.TestCase):
    def test_init__when_string_is_passed(self):
        expected = [1, 3]
        actual = IntegerList(1, 'str', 3).get_data()

        self.assertEqual(expected, actual)

    def test_init__when_only_integers_are_passed(self):
        expected = [1, 2, 3]
        actual = IntegerList(1, 2, 3).get_data()

        self.assertEqual(expected, actual)

    def test_get_data__expect_list_with_integers(self):
        expected = [1, 2, 3]
        actual = IntegerList(1, 2, 3).get_data()

        self.assertEqual(expected, actual)

    def test_add__when_int_is_passed__expect_valid(self):
        expected = [1, 2, 3]
        actual = IntegerList(1, 2).add(3)
        self.assertEqual(expected, actual)

    def test_add__when_not_int_is_passed__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            IntegerList().add('str')

        self.assertEqual("Element is not Integer", str(context.exception))

    def test_remove_index__when_invalid_index__expect_index_error(self):
        with self.assertRaises(IndexError) as context:
            IntegerList(1).remove_index(4)

        self.assertEqual("Index is out of range", str(context.exception))

    def test_remove_index__with_valid_index__expect_valid(self):
        # arrange
        expect = [1, 3]
        ll = IntegerList(1, 2, 3)

        # act
        ll.remove_index(1)

        # assert
        actual = ll.get_data()
        self.assertEqual(expect, actual)

    def test_get__when_invalid_index__expect_index_error(self):
        with self.assertRaises(IndexError) as context:
            IntegerList(1).get(4)

        self.assertEqual("Index is out of range", str(context.exception))

    def test_get__with_valid_index__expect_valid(self):
        # arrange
        expect = 2
        ll = IntegerList(1, 2, 3)
        # act
        actual = ll.get(1)
        # assert
        self.assertEqual(expect, actual)

    def test_insert__with_invalid_index_and_integer__expect_index_error(self):
        with self.assertRaises(IndexError) as context:
            IntegerList(1).insert(2, 2)

        self.assertEqual("Index is out of range", str(context.exception))

    def test_insert__when_not_integer_and_valid_index__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            IntegerList(1, 2, 3).insert(1, 'str')

        self.assertEqual("Element is not Integer", str(context.exception))

    def test_insert__with_valid_index_and_integer__expect_valid(self):
        expect = [1, 2, 3, 4]
        ll = IntegerList(1, 3, 4)

        ll.insert(1, 2)
        actual = ll.get_data()

        self.assertEqual(expect, actual)

    def test_get_biggest__with_1_3_2__expect_3(self):
        self.assertEqual(3, IntegerList(1, 3, 2).get_biggest())

    def test_get_index__with_1_2_3_and_element_2__expect_1(self):
        self.assertEqual(1, IntegerList(1, 2, 3).get_index(2))


if __name__ == '__main__':
    unittest.main()
