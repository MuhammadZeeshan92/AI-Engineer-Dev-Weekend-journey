"""
Demonstrate asynchronous execution using asyncio.
"""

import asyncio
import time


async def fake_download(task_name, delay):
    """
    Simulate downloading data asynchronously.
    """
    print(f"{task_name} started")

    await asyncio.sleep(delay)

    print(f"{task_name} completed")


async def main():
    print("=" * 60)
    print("ASYNCIO DEMO")
    print("=" * 60)

    start = time.perf_counter()

    await asyncio.gather(
        fake_download("Task 1", 2),
        fake_download("Task 2", 2),
        fake_download("Task 3", 2),
    )

    end = time.perf_counter()

    print(f"\nTotal Time: {end - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())