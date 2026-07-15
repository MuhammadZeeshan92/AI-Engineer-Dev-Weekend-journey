"""
Project Demonstration

Run this file to see demonstrations of all implemented
data structures, algorithms, and Big O examples.
"""

from analysis.big_o_examples import demonstrate_big_o

from data_structures.arrays import Array
from data_structures.linked_list import LinkedList
from data_structures.hash_table import HashTable
from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.tree import BinarySearchTree
from data_structures.graph import Graph

from algorithms.searching import linear_search, binary_search
from algorithms.sorting import bubble_sort, quick_sort, merge_sort
from algorithms.recursion import factorial, fibonacci, sum_of_digits


def demonstrate_arrays():
    """Demonstrate array operations."""
    print("\n" + "=" * 60)
    print("ARRAY")
    print("=" * 60)

    array = Array()

    array.append(10)
    array.append(20)
    array.append(30)

    array.insert(1, 15)

    print("Array:", array.display())
    print("Search 20:", array.search(20))

    array.update(2, 25)

    print("Updated:", array.display())

    removed = array.delete(0)
    print("Removed:", removed)
    print("Final:", array.display())


def demonstrate_linked_list():
    """Demonstrate linked list operations."""
    print("\n" + "=" * 60)
    print("LINKED LIST")
    print("=" * 60)

    linked_list = LinkedList()

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)

    print("List:", linked_list.traverse())
    print("Search 20:", linked_list.search(20))

    linked_list.delete(20)

    print("After deletion:", linked_list.traverse())


def demonstrate_hash_table():
    """Demonstrate hash table operations."""
    print("\n" + "=" * 60)
    print("HASH TABLE")
    print("=" * 60)

    table = HashTable()

    table.put("name", "Zeeshan")
    table.put("role", "AI Engineer")

    print(table.display())

    print("Name:", table.get("name"))

    table.remove("role")

    print("After removal:", table.display())


def demonstrate_stack():
    """Demonstrate stack operations."""
    print("\n" + "=" * 60)
    print("STACK")
    print("=" * 60)

    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack:", stack.display())
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("Stack:", stack.display())


def demonstrate_queue():
    """Demonstrate queue operations."""
    print("\n" + "=" * 60)
    print("QUEUE")
    print("=" * 60)

    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Queue:", queue.display())
    print("Front:", queue.front())
    print("Dequeue:", queue.dequeue())
    print("Queue:", queue.display())


def demonstrate_tree():
    """Demonstrate binary search tree."""
    print("\n" + "=" * 60)
    print("BINARY SEARCH TREE")
    print("=" * 60)

    bst = BinarySearchTree()

    for value in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(value)

    print("Inorder:", bst.inorder())
    print("Preorder:", bst.preorder())
    print("Postorder:", bst.postorder())
    print("Search 60:", bst.search(60))


def demonstrate_graph():
    """Demonstrate graph operations."""
    print("\n" + "=" * 60)
    print("GRAPH")
    print("=" * 60)

    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")

    print("Adjacency List:")
    for vertex, neighbors in graph.display().items():
        print(f"{vertex}: {neighbors}")

    print("DFS:", graph.dfs("A"))
    print("BFS:", graph.bfs("A"))


def demonstrate_searching():
    """Demonstrate searching algorithms."""
    print("\n" + "=" * 60)
    print("SEARCHING")
    print("=" * 60)

    numbers = [5, 15, 25, 35, 45]

    print("Linear Search (25):", linear_search(numbers, 25))
    print("Binary Search (35):", binary_search(numbers, 35))


def demonstrate_sorting():
    """Demonstrate sorting algorithms."""
    print("\n" + "=" * 60)
    print("SORTING")
    print("=" * 60)

    numbers = [64, 34, 25, 12, 22, 11, 90]

    print("Original:", numbers)
    print("Bubble:", bubble_sort(numbers))
    print("Quick:", quick_sort(numbers))
    print("Merge:", merge_sort(numbers))


def demonstrate_recursion():
    """Demonstrate recursion examples."""
    print("\n" + "=" * 60)
    print("RECURSION")
    print("=" * 60)

    print("Factorial(5):", factorial(5))
    print("Fibonacci(7):", fibonacci(7))
    print("Sum of Digits(12345):", sum_of_digits(12345))


def main():
    """Run all demonstrations."""

    print("=" * 60)
    print("DATA STRUCTURES & ALGORITHMS PROJECT DEMO")
    print("=" * 60)

    demonstrate_big_o()

    demonstrate_arrays()
    demonstrate_linked_list()
    demonstrate_hash_table()
    demonstrate_stack()
    demonstrate_queue()
    demonstrate_tree()
    demonstrate_graph()

    demonstrate_searching()
    demonstrate_sorting()
    demonstrate_recursion()

    print("\n" + "=" * 60)
    print("ALL DEMONSTRATIONS COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()