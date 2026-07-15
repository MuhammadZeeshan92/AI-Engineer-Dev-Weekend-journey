"""
Benchmark summary for the Concurrency project.

Run the individual examples to compare execution times.
"""

from textwrap import dedent


def main():
    print("=" * 70)
    print("CONCURRENCY BENCHMARK SUMMARY")
    print("=" * 70)

    print(
        dedent(
            """
            Run the following commands from the project root:

            1. Sequential Fetch
               python -m examples.sequential_fetch

            2. Threaded Fetch
               python -m examples.threaded_fetch

            3. Multiprocessing Demo
               python -m examples.multiprocessing_demo

            4. Asyncio Demo
               python -m examples.asyncio_demo
            """
        )
    )

    print("=" * 70)
    print("EXPECTED OBSERVATIONS")
    print("=" * 70)

    print("- Sequential execution performs tasks one after another.")
    print("- Threading significantly improves I/O-bound workloads.")
    print("- Multiprocessing is best suited for CPU-bound tasks.")
    print("- Asyncio efficiently handles many waiting tasks using one thread.")

    print("\nExample timings (will vary by system):")

    print("Sequential      : ~8.38 s")
    print("Threading       : ~1.94 s")
    print("Multiprocessing : ~2-3 s")
    print("Asyncio         : ~2.0 s")

    print("\n" + "=" * 70)
    print("BENCHMARK COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()