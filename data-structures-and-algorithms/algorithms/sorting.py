"""
Sorting Algorithms

This module implements common sorting algorithms including
Bubble Sort, Quick Sort, and Merge Sort.
"""


def bubble_sort(items):
    """
    Sort a list using Bubble Sort.

    Args:
        items: List of comparable elements.

    Returns:
        A new sorted list.

    Time Complexity:
        Best: O(n)
        Average: O(n²)
        Worst: O(n²)

    Space Complexity:
        O(n)
    """
    sorted_items = items.copy()
    n = len(sorted_items)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if sorted_items[j] > sorted_items[j + 1]:
                sorted_items[j], sorted_items[j + 1] = (
                    sorted_items[j + 1],
                    sorted_items[j],
                )
                swapped = True

        if not swapped:
            break

    return sorted_items


def quick_sort(items):
    """
    Sort a list using Quick Sort.

    Args:
        items: List of comparable elements.

    Returns:
        A new sorted list.

    Time Complexity:
        Best: O(n log n)
        Average: O(n log n)
        Worst: O(n²)

    Space Complexity:
        Average: O(log n)
        Worst: O(n)
    """
    if len(items) <= 1:
        return items.copy()

    pivot = items[-1]

    left = [item for item in items[:-1] if item <= pivot]
    right = [item for item in items[:-1] if item > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


def merge_sort(items):
    """
    Sort a list using Merge Sort.

    Args:
        items: List of comparable elements.

    Returns:
        A new sorted list.

    Time Complexity:
        Best: O(n log n)
        Average: O(n log n)
        Worst: O(n log n)

    Space Complexity:
        O(n)
    """
    if len(items) <= 1:
        return items.copy()

    mid = len(items) // 2

    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    return _merge(left, right)


def _merge(left, right):
    """Merge two sorted lists."""
    merged = []

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


def main():
    """Demonstrate sorting algorithms."""

    numbers = [64, 34, 25, 12, 22, 11, 90]

    print("=" * 50)
    print("SORTING ALGORITHMS DEMONSTRATION")
    print("=" * 50)

    print("\nOriginal List:")
    print(numbers)

    print("\nBubble Sort:")
    print(bubble_sort(numbers))

    print("\nQuick Sort:")
    print(quick_sort(numbers))

    print("\nMerge Sort:")
    print(merge_sort(numbers))

    print("\nOriginal List After Sorting:")
    print(numbers)


if __name__ == "__main__":
    main()