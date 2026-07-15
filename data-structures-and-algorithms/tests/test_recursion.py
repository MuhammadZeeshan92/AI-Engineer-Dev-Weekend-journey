import unittest

from algorithms.recursion import factorial, fibonacci, sum_of_digits


class TestRecursion(unittest.TestCase):
    """Tests for recursive algorithms."""

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(7), 13)

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-5)

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(12345), 15)
        self.assertEqual(sum_of_digits(0), 0)

    def test_sum_of_digits_negative(self):
        with self.assertRaises(ValueError):
            sum_of_digits(-123)


if __name__ == "__main__":
    unittest.main()