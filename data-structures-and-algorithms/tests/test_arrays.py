import unittest

from data_structures.arrays import Array


class TestArray(unittest.TestCase):
    """Tests for the Array class."""

    def setUp(self):
        self.array = Array()

    def test_append(self):
        self.array.append(10)
        self.array.append(20)

        self.assertEqual(self.array.display(), [10, 20])

    def test_insert(self):
        self.array.append(10)
        self.array.append(30)

        self.array.insert(1, 20)

        self.assertEqual(self.array.display(), [10, 20, 30])

    def test_delete(self):
        self.array.append(10)
        self.array.append(20)

        removed = self.array.delete(0)

        self.assertEqual(removed, 10)
        self.assertEqual(self.array.display(), [20])

    def test_search(self):
        self.array.append(5)
        self.array.append(15)

        self.assertEqual(self.array.search(15), 1)
        self.assertEqual(self.array.search(100), -1)

    def test_update(self):
        self.array.append(10)

        self.array.update(0, 99)

        self.assertEqual(self.array.get(0), 99)


if __name__ == "__main__":
    unittest.main()