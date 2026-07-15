"""
Array Implementation

This module demonstrates common array operations using Python lists.
Python lists are dynamic arrays that automatically resize as elements
are added or removed.
"""


class Array:
    """A simple array implementation using a Python list."""

    def __init__(self):
        """Initialize an empty array."""
        self.items = []

    def append(self, value):
        """
        Add an element to the end of the array.

        Time Complexity:
            O(1) amortized

        Space Complexity:
            O(1)
        """
        self.items.append(value)

    def insert(self, index, value):
        """
        Insert an element at a specific index.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """
        if index < 0 or index > len(self.items):
            raise IndexError("Index out of range")

        self.items.insert(index, value)

    def delete(self, index):
        """
        Remove an element by index.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of range")

        return self.items.pop(index)

    def search(self, value):
        """
        Find the index of a value.

        Returns:
            Index if found, otherwise -1.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """
        for index, item in enumerate(self.items):
            if item == value:
                return index

        return -1

    def update(self, index, value):
        """
        Update the value at a given index.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of range")

        self.items[index] = value

    def get(self, index):
        """
        Return the value at a given index.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of range")

        return self.items[index]

    def display(self):
        """
        Return all array elements.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return self.items.copy()

    def size(self):
        """
        Return the number of elements.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return len(self.items)

    def is_empty(self):
        """
        Check whether the array is empty.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return len(self.items) == 0


def main():
    """Demonstrate array operations."""

    array = Array()

    print("=" * 50)
    print("ARRAY DEMONSTRATION")
    print("=" * 50)

    print("\nAppending elements...")
    array.append(10)
    array.append(20)
    array.append(30)
    print(array.display())

    print("\nInserting 15 at index 1...")
    array.insert(1, 15)
    print(array.display())

    print("\nSearching for 20...")
    print("Index:", array.search(20))

    print("\nUpdating index 2 to 25...")
    array.update(2, 25)
    print(array.display())

    print("\nElement at index 1:")
    print(array.get(1))

    print("\nDeleting index 0...")
    removed = array.delete(0)
    print("Removed:", removed)
    print(array.display())

    print("\nArray size:", array.size())
    print("Is empty:", array.is_empty())


if __name__ == "__main__":
    main()