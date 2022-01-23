from worker import Worker

import unittest


class WorkerTests(unittest.TestCase):
    valid_name = 'Test Worker'
    valid_salary = 1000
    valid_energy = 100

    def test_init__expect_valid(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        self.assertEqual(self.valid_name, worker.name)
        self.assertEqual(self.valid_salary, worker.salary)
        self.assertEqual(self.valid_energy, worker.energy)
        self.assertEqual(0, worker.money)

    def test_rest__with_1_increase__expect_valid(self):
        # arrange
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        expected_energy = self.valid_energy + 1

        # act
        worker.rest()
        actual_energy = worker.energy

        # assert
        self.assertEqual(expected_energy, actual_energy)

    def test_work_money__when_energy_is_positive__expect_valid(self):
        # arrange
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        expected_money = 0 + self.valid_salary

        # act
        worker.work()

        # assert
        actual_money = worker.money
        self.assertEqual(expected_money, actual_money)

    def test_work_energy__when_energy_is_positive__expect_valid(self):
        # arrange
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        expected_energy = self.valid_energy - 1

        # act
        worker.work()

        # assert
        actual_energy = worker.energy
        self.assertEqual(expected_energy, actual_energy)

    def test_work__when_energy_is_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            Worker(self.valid_name, self.valid_salary, 0).work()

        self.assertEqual('Not enough energy.', str(context.exception))

    def test_work__when_energy_is_negative__expect_exception(self):
        with self.assertRaises(Exception) as context:
            Worker(self.valid_name, self.valid_salary, -1).work()

        self.assertEqual('Not enough energy.', str(context.exception))

    def test_get_info__with_correct_values__expect_valid(self):
        # arrange
        expected = f'{self.valid_name} has saved {0} money.'
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        # act
        actual = worker.get_info()

        # assert
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
