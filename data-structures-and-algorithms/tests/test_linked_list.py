import unittest

from data_structures.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    """Tests for the LinkedList class."""

    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert_at_end(self):
        self.linked_list.insert_at_end(10)
        self.linked_list.insert_at_end(20)

        self.assertEqual(self.linked_list.traverse(), [10, 20])

    def test_insert_at_beginning(self):
        self.linked_list.insert_at_beginning(20)
        self.linked_list.insert_at_beginning(10)

        self.assertEqual(self.linked_list.traverse(), [10, 20])

    def test_search(self):
        self.linked_list.insert_at_end(10)

        self.assertTrue(self.linked_list.search(10))
        self.assertFalse(self.linked_list.search(50))

    def test_delete(self):
        self.linked_list.insert_at_end(10)
        self.linked_list.insert_at_end(20)

        self.assertTrue(self.linked_list.delete(10))
        self.assertEqual(self.linked_list.traverse(), [20])


if __name__ == "__main__":
    unittest.main()