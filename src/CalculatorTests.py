import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(selfself):
        calculator = calculator()
        self.assertIsInstance(calculator, Calculator)


if __name__ == '__main__':
    unittest.main()