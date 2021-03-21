import unittest
from CsvReader import CsvReader, ClassFactory
from CalculatorTests import Calculator


# Addition

class AdditionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('addition.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__)


if __name__ == '__main__':
    unittest.main()


# Subtraction

class SubtractionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('/src/subtraction.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__)


if __name__ == '__main__':
    unittest.main()


# Multiplication

class MultiplicationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('/src/multiplication.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__)


if __name__ == '__main__':
    unittest.main()


# Division

class DivisionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('/src/division.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__)


if __name__ == '__main__':
    unittest.main()
