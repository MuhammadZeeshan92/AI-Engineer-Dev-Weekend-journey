"""
Big O Analysis Examples

This module demonstrates common time and space complexities
using simple Python functions. The implementations are
educational and intended to build intuition about algorithm
performance.
"""


def constant_time(numbers):
    """
    Return the first element of the list.

    Time Complexity:
        O(1)

    Space Complexity:
        O(1)
    """
    return numbers[0] if numbers else None


def logarithmic_time(sorted_numbers, target):
    """
    Perform binary search on a sorted list.

    Time Complexity:
        O(log n)

    Space Complexity:
        O(1)
    """
    left = 0
    right = len(sorted_numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_numbers[mid] == target:
            return mid

        if sorted_numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def linear_time(numbers):
    """
    Calculate the sum of all elements.

    Time Complexity:
        O(n)

    Space Complexity:
        O(1)
    """
    total = 0

    for number in numbers:
        total += number

    return total


def linearithmic_time(numbers):
    """
    Return a sorted copy of the list.

    Python's built-in sorted() uses Timsort.

    Time Complexity:
        O(n log n)

    Space Complexity:
        O(n)
    """
    return sorted(numbers)


def quadratic_time(numbers):
    """
    Print every possible pair of elements.

    Time Complexity:
        O(n²)

    Space Complexity:
        O(1)
    """
    pairs = []

    for first in numbers:
        for second in numbers:
            pairs.append((first, second))

    return pairs


def linear_space(numbers):
    """
    Create a new list with doubled values.

    Time Complexity:
        O(n)

    Space Complexity:
        O(n)
    """
    doubled = []

    for number in numbers:
        doubled.append(number * 2)

    return doubled


def demonstrate_big_o():
    """Run demonstrations of each complexity example."""

    sample = [3, 8, 2, 9, 5, 1]
    sorted_sample = sorted(sample)

    print("=" * 50)
    print("BIG O ANALYSIS DEMONSTRATION")
    print("=" * 50)

    print(f"\nSample List: {sample}")

    print("\nO(1) - Constant Time")
    print("First Element:", constant_time(sample))

    print("\nO(log n) - Logarithmic Time")
    index = logarithmic_time(sorted_sample, 5)
    print(f"Sorted List: {sorted_sample}")
    print(f"Index of 5: {index}")

    print("\nO(n) - Linear Time")
    print("Sum:", linear_time(sample))

    print("\nO(n log n) - Linearithmic Time")
    print("Sorted:", linearithmic_time(sample))

    print("\nO(n²) - Quadratic Time")
    pairs = quadratic_time([1, 2, 3])
    print(f"Pairs Generated: {pairs}")

    print("\nO(n) Space Complexity")
    print("Doubled Values:", linear_space(sample))


if __name__ == "__main__":
    demonstrate_big_o()