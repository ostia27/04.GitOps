from unittest import TestCase, main
from calculator import Calculator


class TestCalculator(TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(6, 9), 15)
        self.assertEqual(Calculator.add(79, 31), 110)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(0, 0), 0)
        self.assertEqual(Calculator.subtract(6, 9), -3)
        self.assertEqual(Calculator.subtract(-6, -10), 4)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 9), 18)
        self.assertEqual(Calculator.multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(Calculator.divide(15, 3), 5)
        with self.assertRaises(ZeroDivisionError):
            Calculator.divide(15, 0)

if __name__ == '__main__':
    main()