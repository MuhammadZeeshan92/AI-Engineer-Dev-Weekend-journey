"""
Graph Implementation

This module implements an undirected graph using an adjacency list.
It also provides Depth-First Search (DFS) and Breadth-First Search (BFS)
traversal algorithms.
"""

from collections import deque


class Graph:
    """
    A simple undirected graph implemented using an adjacency list.
    """

    def __init__(self):
        """
        Initialize an empty graph.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        self.graph = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, source, destination):
        """
        Add an undirected edge between two vertices.

        If a vertex does not exist, it is created automatically.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        self.add_vertex(source)
        self.add_vertex(destination)

        if destination not in self.graph[source]:
            self.graph[source].append(destination)

        if source not in self.graph[destination]:
            self.graph[destination].append(source)

    def dfs(self, start):
        """
        Perform Depth-First Search (DFS).

        Returns:
            List of visited vertices.

        Time Complexity:
            O(V + E)

        Space Complexity:
            O(V)
        """
        if start not in self.graph:
            return []

        visited = set()
        traversal = []

        self._dfs(start, visited, traversal)

        return traversal

    def _dfs(self, vertex, visited, traversal):
        """Recursive helper for DFS."""
        visited.add(vertex)
        traversal.append(vertex)

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs(neighbor, visited, traversal)

    def bfs(self, start):
        """
        Perform Breadth-First Search (BFS).

        Returns:
            List of visited vertices.

        Time Complexity:
            O(V + E)

        Space Complexity:
            O(V)
        """
        if start not in self.graph:
            return []

        visited = {start}
        traversal = []
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            traversal.append(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal

    def display(self):
        """
        Return the adjacency list.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return self.graph


def main():
    """Demonstrate graph operations."""

    graph = Graph()

    print("=" * 50)
    print("GRAPH DEMONSTRATION")
    print("=" * 50)

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "F")
    graph.add_edge("E", "F")

    print("\nAdjacency List:")
    for vertex, neighbors in graph.display().items():
        print(f"{vertex}: {neighbors}")

    print("\nDepth-First Search (DFS) starting from A:")
    print(graph.dfs("A"))

    print("\nBreadth-First Search (BFS) starting from A:")
    print(graph.bfs("A"))


if __name__ == "__main__":
    main()