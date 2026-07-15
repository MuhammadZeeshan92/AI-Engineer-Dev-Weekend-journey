import unittest

from algorithms.sorting import bubble_sort, merge_sort, quick_sort


class TestSorting(unittest.TestCase):
    """Tests for sorting algorithms."""

    def setUp(self):
        self.numbers = [64, 34, 25, 12, 22, 11, 90]
        self.sorted_numbers = sorted(self.numbers)

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(self.numbers), self.sorted_numbers)

    def test_quick_sort(self):
        self.assertEqual(quick_sort(self.numbers), self.sorted_numbers)

    def test_merge_sort(self):
        self.assertEqual(merge_sort(self.numbers), self.sorted_numbers)

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(bubble_sort([5]), [5])
        self.assertEqual(quick_sort([5]), [5])
        self.assertEqual(merge_sort([5]), [5])

    def test_original_list_unchanged(self):
        original = self.numbers.copy()

        bubble_sort(self.numbers)
        quick_sort(self.numbers)
        merge_sort(self.numbers)

        self.assertEqual(self.numbers, original)


if __name__ == "__main__":
    unittest.main()