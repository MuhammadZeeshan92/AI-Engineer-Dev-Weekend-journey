import unittest

from algorithms.searching import binary_search, linear_search


class TestSearching(unittest.TestCase):
    """Tests for searching algorithms."""

    def setUp(self):
        self.unsorted_numbers = [25, 10, 40, 5, 30, 15]
        self.sorted_numbers = sorted(self.unsorted_numbers)

    def test_linear_search_found(self):
        self.assertEqual(linear_search(self.unsorted_numbers, 30), 4)

    def test_linear_search_not_found(self):
        self.assertEqual(linear_search(self.unsorted_numbers, 100), -1)

    def test_binary_search_found(self):
        index = binary_search(self.sorted_numbers, 30)

        self.assertNotEqual(index, -1)
        self.assertEqual(self.sorted_numbers[index], 30)

    def test_binary_search_not_found(self):
        self.assertEqual(binary_search(self.sorted_numbers, 100), -1)


if __name__ == "__main__":
    unittest.main()