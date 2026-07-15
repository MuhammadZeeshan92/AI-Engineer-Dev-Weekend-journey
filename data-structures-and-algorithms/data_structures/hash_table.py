"""
Hash Table Implementation

This module implements a simple hash table using separate chaining
to handle collisions.
"""


class HashTable:
    """
    A simple hash table implementation.
    """

    def __init__(self, capacity=10):
        """
        Initialize the hash table.

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)
        """
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key):
        """
        Generate the index for a given key.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return hash(key) % self.capacity

    def put(self, key, value):
        """
        Insert or update a key-value pair.

        Time Complexity:
            Average: O(1)
            Worst: O(n)

        Space Complexity:
            O(1)
        """
        index = self._hash(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])

    def get(self, key):
        """
        Retrieve the value associated with a key.

        Returns:
            Value if found, otherwise None.

        Time Complexity:
            Average: O(1)
            Worst: O(n)

        Space Complexity:
            O(1)
        """
        index = self._hash(key)
        bucket = self.table[index]

        for stored_key, stored_value in bucket:
            if stored_key == key:
                return stored_value

        return None

    def remove(self, key):
        """
        Remove a key-value pair.

        Returns:
            True if removed, otherwise False.

        Time Complexity:
            Average: O(1)
            Worst: O(n)

        Space Complexity:
            O(1)
        """
        index = self._hash(key)
        bucket = self.table[index]

        for i, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket.pop(i)
                return True

        return False

    def contains(self, key):
        """
        Check whether a key exists.

        Time Complexity:
            Average: O(1)
            Worst: O(n)

        Space Complexity:
            O(1)
        """
        return self.get(key) is not None

    def display(self):
        """
        Display the contents of the hash table.

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)
        """
        return self.table


def main():
    """Demonstrate hash table operations."""

    hash_table = HashTable()

    print("=" * 50)
    print("HASH TABLE DEMONSTRATION")
    print("=" * 50)

    print("\nAdding key-value pairs...")
    hash_table.put("name", "Zeeshan")
    hash_table.put("age", 22)
    hash_table.put("city", "Lahore")

    print(hash_table.display())

    print("\nRetrieve values:")
    print("name:", hash_table.get("name"))
    print("age:", hash_table.get("age"))
    print("city:", hash_table.get("city"))

    print("\nUpdate age...")
    hash_table.put("age", 23)
    print("Updated age:", hash_table.get("age"))

    print("\nContains 'city'?")
    print(hash_table.contains("city"))

    print("\nRemove 'city'...")
    hash_table.remove("city")

    print("Contains 'city'?")
    print(hash_table.contains("city"))

    print("\nFinal Hash Table:")
    print(hash_table.display())


if __name__ == "__main__":
    main()