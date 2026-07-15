"""
Fetch data from multiple URLs concurrently using ThreadPoolExecutor.
"""

import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

from urls import URLS


def fetch_url(url):
    """
    Fetch data from a single URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        dict: JSON response.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    print("=" * 60)
    print("THREADED URL FETCHING")
    print("=" * 60)

    start_time = time.perf_counter()

    with ThreadPoolExecutor(max_workers=5) as executor:

        futures = [
            executor.submit(fetch_url, url)
            for url in URLS
        ]

        for future in as_completed(futures):
            data = future.result()
            print(f"Post ID: {data['id']} | Title: {data['title']}")

    end_time = time.perf_counter()

    print("\n" + "=" * 60)
    print(f"Total Time: {end_time - start_time:.2f} seconds")
    print("=" * 60)


if __name__ == "__main__":
    main()