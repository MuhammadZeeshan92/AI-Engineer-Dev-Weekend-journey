"""
Searching Algorithms

This module implements common searching algorithms including
Linear Search and Binary Search.
"""


def linear_search(items, target):
    """
    Search for a target value using Linear Search.

    Args:
        items: List of elements.
        target: Value to search for.

    Returns:
        Index of the target if found, otherwise -1.

    Time Complexity:
        Best: O(1)
        Average: O(n)
        Worst: O(n)

    Space Complexity:
        O(1)
    """
    for index, item in enumerate(items):
        if item == target:
            return index

    return -1


def binary_search(sorted_items, target):
    """
    Search for a target value using Binary Search.

    Note:
        The input list must already be sorted.

    Args:
        sorted_items: Sorted list of elements.
        target: Value to search for.

    Returns:
        Index of the target if found, otherwise -1.

    Time Complexity:
        Best: O(1)
        Average: O(log n)
        Worst: O(log n)

    Space Complexity:
        O(1)
    """
    left = 0
    right = len(sorted_items) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_items[mid] == target:
            return mid

        if sorted_items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    """Demonstrate searching algorithms."""

    numbers = [25, 10, 40, 5, 30, 15]
    sorted_numbers = sorted(numbers)

    print("=" * 50)
    print("SEARCHING ALGORITHMS DEMONSTRATION")
    print("=" * 50)

    print("\nOriginal List:")
    print(numbers)

    print("\nLinear Search")
    target = 30
    index = linear_search(numbers, target)

    if index != -1:
        print(f"{target} found at index {index}")
    else:
        print(f"{target} not found")

    print("\nSorted List:")
    print(sorted_numbers)

    print("\nBinary Search")
    target = 30
    index = binary_search(sorted_numbers, target)

    if index != -1:
        print(f"{target} found at index {index}")
    else:
        print(f"{target} not found")

    print("\nSearching for a missing value:")
    target = 100

    print(f"Linear Search: {linear_search(numbers, target)}")
    print(f"Binary Search: {binary_search(sorted_numbers, target)}")


if __name__ == "__main__":
    main()