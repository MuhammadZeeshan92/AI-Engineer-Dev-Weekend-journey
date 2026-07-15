import unittest

from data_structures.queue import Queue


class TestQueue(unittest.TestCase):
    """Tests for the Queue class."""

    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)

        self.assertEqual(self.queue.display(), [10, 20])

    def test_dequeue(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)

        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.display(), [20])

    def test_front(self):
        self.queue.enqueue(5)
        self.queue.enqueue(15)

        self.assertEqual(self.queue.front(), 5)

    def test_rear(self):
        self.queue.enqueue(5)
        self.queue.enqueue(15)

        self.assertEqual(self.queue.rear(), 15)

    def test_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()


if __name__ == "__main__":
    unittest.main()