import unittest

from data_structures.tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    """Tests for the BinarySearchTree class."""

    def setUp(self):
        self.bst = BinarySearchTree()

        for value in [50, 30, 70, 20, 40, 60, 80]:
            self.bst.insert(value)

    def test_search(self):
        self.assertTrue(self.bst.search(60))
        self.assertFalse(self.bst.search(100))

    def test_inorder(self):
        self.assertEqual(
            self.bst.inorder(),
            [20, 30, 40, 50, 60, 70, 80]
        )

    def test_preorder(self):
        self.assertEqual(
            self.bst.preorder(),
            [50, 30, 20, 40, 70, 60, 80]
        )

    def test_postorder(self):
        self.assertEqual(
            self.bst.postorder(),
            [20, 40, 30, 60, 80, 70, 50]
        )


if __name__ == "__main__":
    unittest.main()