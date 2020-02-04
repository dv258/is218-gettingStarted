import unittest

from Calculator.Calculator import Calculator


class TestCases(unittest.TestCase):
    def test_instantiate(self):
        calc = Calculator()

        self.assertIsInstance(calc, Calculator)

    def test_add(self):
        calc = Calculator()

        result = calc.add(2, 2)
        self.assertEqual(4, result)

    def test_subtract(self):
        calc = Calculator()

        result = calc.subtract(7, 4)
        self.assertEqual(3, result)

    def test_multiply(self):
        calc = Calculator()

        result = calc.multiply(-2, 6)
        self.assertEqual(-12, result)

    def test_divide(self):
        calc = Calculator()

        result = calc.divide(8, 4)
        self.assertEqual(2, result)

    def test_sqrt(self):
        calc = Calculator()

        result = calc.sqrt(16)
        self.assertEqual(4, result)

    def test_square(self):
        calc = Calculator()

        result = calc.square(7)
        self.assertEqual(49, result)


if __name__ == "__main__":
    unittest.main()
