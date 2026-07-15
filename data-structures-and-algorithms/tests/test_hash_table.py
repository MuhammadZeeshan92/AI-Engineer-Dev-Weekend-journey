import unittest

from data_structures.hash_table import HashTable


class TestHashTable(unittest.TestCase):
    """Tests for the HashTable class."""

    def setUp(self):
        self.hash_table = HashTable()

    def test_put_and_get(self):
        self.hash_table.put("name", "Zeeshan")

        self.assertEqual(self.hash_table.get("name"), "Zeeshan")

    def test_update_existing_key(self):
        self.hash_table.put("age", 22)
        self.hash_table.put("age", 23)

        self.assertEqual(self.hash_table.get("age"), 23)

    def test_remove(self):
        self.hash_table.put("city", "Lahore")

        self.assertTrue(self.hash_table.remove("city"))
        self.assertIsNone(self.hash_table.get("city"))

    def test_contains(self):
        self.hash_table.put("language", "Python")

        self.assertTrue(self.hash_table.contains("language"))
        self.assertFalse(self.hash_table.contains("Java"))


if __name__ == "__main__":
    unittest.main()