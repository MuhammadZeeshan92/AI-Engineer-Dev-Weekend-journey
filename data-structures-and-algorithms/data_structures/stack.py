"""
Stack Implementation

This module implements a stack using a Python list.
A stack follows the Last In, First Out (LIFO) principle.
"""


class Stack:
    """
    A simple stack implementation.
    """

    def __init__(self):
        """
        Initialize an empty stack.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        self.items = []

    def push(self, item):
        """
        Push an item onto the stack.

        Time Complexity:
            O(1) amortized

        Space Complexity:
            O(1)
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top element.

        Returns:
            The top element.

        Raises:
            IndexError: If the stack is empty.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")

        return self.items.pop()

    def peek(self):
        """
        Return the top element without removing it.

        Raises:
            IndexError: If the stack is empty.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        if self.is_empty():
            raise IndexError("Stack is empty.")

        return self.items[-1]

    def is_empty(self):
        """
        Check whether the stack is empty.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the number of elements in the stack.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return len(self.items)

    def display(self):
        """
        Return the stack contents from bottom to top.

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)
        """
        return self.items.copy()


def main():
    """Demonstrate stack operations."""

    stack = Stack()

    print("=" * 50)
    print("STACK DEMONSTRATION")
    print("=" * 50)

    print("\nIs stack empty?")
    print(stack.is_empty())

    print("\nPushing elements...")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    print("Stack:", stack.display())

    print("\nTop element:")
    print(stack.peek())

    print("\nStack size:")
    print(stack.size())

    print("\nPopping elements...")
    print(stack.pop())
    print(stack.pop())

    print("\nCurrent stack:")
    print(stack.display())

    print("\nTop element:")
    print(stack.peek())

    print("\nIs stack empty?")
    print(stack.is_empty())


if __name__ == "__main__":
    main()