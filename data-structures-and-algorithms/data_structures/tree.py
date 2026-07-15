"""
Binary Search Tree (BST) Implementation

This module implements a Binary Search Tree (BST) from scratch.
A BST maintains the property that:
- Values smaller than a node are stored in the left subtree.
- Values greater than a node are stored in the right subtree.
"""


class TreeNode:
    """
    Represents a single node in a Binary Search Tree.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    A simple Binary Search Tree implementation.
    """

    def __init__(self):
        """
        Initialize an empty Binary Search Tree.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.

        Time Complexity:
            Average: O(log n)
            Worst: O(n)

        Space Complexity:
            O(1)
        """
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        """Recursive helper method for insertion."""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def search(self, value):
        """
        Search for a value in the BST.

        Returns:
            True if found, otherwise False.

        Time Complexity:
            Average: O(log n)
            Worst: O(n)

        Space Complexity:
            O(1)
        """
        return self._search(self.root, value)

    def _search(self, node, value):
        """Recursive helper method for searching."""
        if node is None:
            return False

        if node.value == value:
            return True

        if value < node.value:
            return self._search(node.left, value)

        return self._search(node.right, value)

    def inorder(self):
        """
        Return the inorder traversal.

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)
        """
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        """Recursive helper for inorder traversal."""
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def preorder(self):
        """
        Return the preorder traversal.

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)
        """
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        """Recursive helper for preorder traversal."""
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        """
        Return the postorder traversal.

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)
        """
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        """Recursive helper for postorder traversal."""
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)


def main():
    """Demonstrate Binary Search Tree operations."""

    bst = BinarySearchTree()

    print("=" * 50)
    print("BINARY SEARCH TREE DEMONSTRATION")
    print("=" * 50)

    values = [50, 30, 70, 20, 40, 60, 80]

    print("\nInserting values:")
    print(values)

    for value in values:
        bst.insert(value)

    print("\nSearch for 40:")
    print(bst.search(40))

    print("\nSearch for 90:")
    print(bst.search(90))

    print("\nInorder Traversal:")
    print(bst.inorder())

    print("\nPreorder Traversal:")
    print(bst.preorder())

    print("\nPostorder Traversal:")
    print(bst.postorder())


if __name__ == "__main__":
    main()