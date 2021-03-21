import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


# Addition

class AdditionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CsvReader('/src/addition.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()


# Subtraction

class SubtractionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        data_frame = CsvReader('/src/subtraction.csv').data
        pprint(data_frame)
        for row in data_frame:
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()


# Multiplication

class MultiplicationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_multiply(self):
        multiply_data = CsvReader('/src/multiplication.csv').data
        for row in multiply_data:
            self.assertEqual(self.calculator.multiply(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()


# Division

class DivisionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_division(self):
        divide_data = CsvReader('src/division.csv').data
        for row in divide_data:
            self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()