import unittest

from data_structures.stack import Stack


class TestStack(unittest.TestCase):
    """Tests for the Stack class."""

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(10)
        self.stack.push(20)

        self.assertEqual(self.stack.display(), [10, 20])

    def test_pop(self):
        self.stack.push(10)
        self.stack.push(20)

        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.display(), [10])

    def test_peek(self):
        self.stack.push(100)

        self.assertEqual(self.stack.peek(), 100)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

        self.stack.push(1)

        self.assertFalse(self.stack.is_empty())

    def test_pop_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.pop()


if __name__ == "__main__":
    unittest.main()