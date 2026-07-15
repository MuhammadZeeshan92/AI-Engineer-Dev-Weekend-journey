"""
Fetch data from multiple URLs sequentially and measure execution time.
"""

import time

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
    print("SEQUENTIAL URL FETCHING")
    print("=" * 60)

    start_time = time.perf_counter()

    for index, url in enumerate(URLS, start=1):
        data = fetch_url(url)
        print(f"{index}. Post ID: {data['id']} | Title: {data['title']}")

    end_time = time.perf_counter()

    print("\n" + "=" * 60)
    print(f"Total Time: {end_time - start_time:.2f} seconds")
    print("=" * 60)


if __name__ == "__main__":
    main()