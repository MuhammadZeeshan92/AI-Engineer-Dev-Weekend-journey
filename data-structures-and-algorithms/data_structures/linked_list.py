"""
Singly Linked List Implementation

This module implements a singly linked list from scratch using nodes.
Each node stores data and a reference to the next node.
"""


class Node:
    """
    Represents a single node in a linked list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A simple singly linked list implementation.
    """

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def is_empty(self):
        """
        Check whether the linked list is empty.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return self.head is None

    def insert_at_beginning(self, data):
        """
        Insert a node at the beginning.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a node at the end.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def search(self, data):
        """
        Search for a value.

        Returns:
            True if found, otherwise False.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """
        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    def delete(self, data):
        """
        Delete the first occurrence of a value.

        Returns:
            True if deleted, otherwise False.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """
        if self.head is None:
            return False

        if self.head.data == data:
            self.head = self.head.next
            return True

        previous = self.head
        current = self.head.next

        while current:
            if current.data == data:
                previous.next = current.next
                return True

            previous = current
            current = current.next

        return False

    def traverse(self):
        """
        Return all elements as a list.

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)
        """
        elements = []
        current = self.head

        while current:
            elements.append(current.data)
            current = current.next

        return elements

    def size(self):
        """
        Return the number of nodes.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count


def main():
    """Demonstrate linked list operations."""

    linked_list = LinkedList()

    print("=" * 50)
    print("LINKED LIST DEMONSTRATION")
    print("=" * 50)

    print("\nInitially:")
    print(linked_list.traverse())

    print("\nInsert at beginning:")
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_beginning(10)
    print(linked_list.traverse())

    print("\nInsert at end:")
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)
    print(linked_list.traverse())

    print("\nSearch for 30:")
    print(linked_list.search(30))

    print("\nSearch for 100:")
    print(linked_list.search(100))

    print("\nDelete 20:")
    linked_list.delete(20)
    print(linked_list.traverse())

    print("\nDelete 10:")
    linked_list.delete(10)
    print(linked_list.traverse())

    print("\nList size:")
    print(linked_list.size())

    print("\nIs empty:")
    print(linked_list.is_empty())


if __name__ == "__main__":
    main()