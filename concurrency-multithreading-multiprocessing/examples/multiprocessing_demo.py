"""
Demonstrate multiprocessing for CPU-bound tasks.
"""

import time
from concurrent.futures import ProcessPoolExecutor


def sum_of_squares(limit):
    """
    Compute the sum of squares from 1 to limit.
    """
    total = 0

    for number in range(1, limit + 1):
        total += number * number

    return total


def main():
    numbers = [
        8_000_000,
        8_000_000,
        8_000_000,
        8_000_000,
    ]

    print("=" * 60)
    print("MULTIPROCESSING DEMO")
    print("=" * 60)

    start = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(sum_of_squares, numbers))

    end = time.perf_counter()

    print("Tasks Completed:", len(results))
    print(f"Total Time: {end - start:.2f} seconds")


if __name__ == "__main__":
    main()