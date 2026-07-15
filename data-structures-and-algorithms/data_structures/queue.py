"""
Queue Implementation

This module implements a queue using a Python list.
A queue follows the First In, First Out (FIFO) principle.
"""


class Queue:
    """
    A simple queue implementation.
    """

    def __init__(self):
        """
        Initialize an empty queue.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        self.items = []

    def enqueue(self, item):
        """
        Add an element to the rear of the queue.

        Time Complexity:
            O(1) amortized

        Space Complexity:
            O(1)
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the front element.

        Raises:
            IndexError: If the queue is empty.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")

        return self.items.pop(0)

    def front(self):
        """
        Return the front element without removing it.

        Raises:
            IndexError: If the queue is empty.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty.")

        return self.items[0]

    def rear(self):
        """
        Return the last element without removing it.

        Raises:
            IndexError: If the queue is empty.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty.")

        return self.items[-1]

    def is_empty(self):
        """
        Check whether the queue is empty.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the number of elements in the queue.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return len(self.items)

    def display(self):
        """
        Return the queue contents from front to rear.

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)
        """
        return self.items.copy()


def main():
    """Demonstrate queue operations."""

    queue = Queue()

    print("=" * 50)
    print("QUEUE DEMONSTRATION")
    print("=" * 50)

    print("\nIs queue empty?")
    print(queue.is_empty())

    print("\nEnqueuing elements...")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)

    print("Queue:", queue.display())

    print("\nFront element:")
    print(queue.front())

    print("Rear element:")
    print(queue.rear())

    print("\nQueue size:")
    print(queue.size())

    print("\nDequeuing elements...")
    print(queue.dequeue())
    print(queue.dequeue())

    print("\nCurrent queue:")
    print(queue.display())

    print("\nFront element:")
    print(queue.front())

    print("\nRear element:")
    print(queue.rear())

    print("\nIs queue empty?")
    print(queue.is_empty())


if __name__ == "__main__":
    main()