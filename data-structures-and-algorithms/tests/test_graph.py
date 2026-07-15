import unittest

from data_structures.graph import Graph


class TestGraph(unittest.TestCase):
    """Tests for the Graph class."""

    def setUp(self):
        self.graph = Graph()

        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")
        self.graph.add_edge("B", "D")

    def test_add_vertex(self):
        self.graph.add_vertex("E")

        self.assertIn("E", self.graph.display())

    def test_dfs(self):
        traversal = self.graph.dfs("A")

        self.assertEqual(traversal, ["A", "B", "D", "C"])

    def test_bfs(self):
        traversal = self.graph.bfs("A")

        self.assertEqual(traversal, ["A", "B", "C", "D"])


if __name__ == "__main__":
    unittest.main()