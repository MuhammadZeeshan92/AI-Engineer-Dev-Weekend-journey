"""
Recursion Examples

This module demonstrates recursion by solving three classic problems:
- Factorial
- Fibonacci
- Sum of Digits
"""


def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n.

    Raises:
        ValueError: If n is negative.

    Time Complexity:
        O(n)

    Space Complexity:
        O(n)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def fibonacci(n):
    """
    Return the nth Fibonacci number.

    Args:
        n: Position in the Fibonacci sequence.

    Returns:
        The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.

    Time Complexity:
        O(2^n)

    Space Complexity:
        O(n)
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_digits(number):
    """
    Calculate the sum of all digits in a positive integer.

    Args:
        number: A non-negative integer.

    Returns:
        Sum of its digits.

    Raises:
        ValueError: If number is negative.

    Time Complexity:
        O(d), where d is the number of digits.

    Space Complexity:
        O(d)
    """
    if number < 0:
        raise ValueError("Number must be non-negative.")

    if number < 10:
        return number

    return number % 10 + sum_of_digits(number // 10)


def main():
    """Demonstrate recursive algorithms."""

    print("=" * 50)
    print("RECURSION DEMONSTRATION")
    print("=" * 50)

    print("\nFactorial")
    number = 5
    print(f"{number}! = {factorial(number)}")

    print("\nFibonacci")
    position = 7
    print(f"Fibonacci({position}) = {fibonacci(position)}")

    print("\nSum of Digits")
    value = 12345
    print(f"Sum of digits of {value} = {sum_of_digits(value)}")


if __name__ == "__main__":
    main()