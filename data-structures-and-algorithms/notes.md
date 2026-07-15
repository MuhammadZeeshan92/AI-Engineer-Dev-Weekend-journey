# Data Structures & Algorithms - Revision Notes

## Overview

Data Structures organize and store data efficiently, while Algorithms define the steps used to solve problems. Understanding both is essential for writing efficient programs, technical interviews, and understanding how software frameworks are built.

---

# Big O Notation

Big O describes how an algorithm's performance changes as the input size increases.

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Access array element |
| O(log n) | Logarithmic | Binary Search |
| O(n) | Linear | Linear Search |
| O(n log n) | Linearithmic | Merge Sort, Quick Sort (average) |
| O(n²) | Quadratic | Bubble Sort |
| O(2ⁿ) | Exponential | Recursive Fibonacci |

Always consider both:

- Time Complexity
- Space Complexity

---

# Arrays

- Store elements in contiguous memory.
- Fast indexing using positions.
- Efficient for random access.
- Insertion and deletion may require shifting elements.

Common Operations:

- Append
- Insert
- Delete
- Search
- Update

---

# Linked Lists

A Linked List consists of nodes connected through references.

Advantages:

- Dynamic size
- Efficient insertion and deletion

Disadvantages:

- Sequential access only
- Extra memory for pointers

---

# Hash Tables

Store data as key-value pairs.

Advantages:

- Average O(1) lookup
- Efficient insertion and deletion

Collision handling techniques include:

- Chaining
- Open Addressing

---

# Stack

Follows LIFO (Last In, First Out).

Operations:

- Push
- Pop
- Peek

Applications:

- Undo functionality
- Function calls
- Expression evaluation

---

# Queue

Follows FIFO (First In, First Out).

Operations:

- Enqueue
- Dequeue
- Front
- Rear

Applications:

- Scheduling
- BFS
- Task processing

---

# Binary Search Tree (BST)

Properties:

- Left subtree contains smaller values.
- Right subtree contains larger values.

Traversals:

- Inorder
- Preorder
- Postorder

Average Operations:

- Search: O(log n)
- Insert: O(log n)

Worst Case:

- O(n)

---

# Graph

Implemented using an adjacency list.

Traversals:

- DFS (Depth-First Search)
- BFS (Breadth-First Search)

Applications:

- Routing
- Social networks
- Recommendation systems

---

# Searching Algorithms

## Linear Search

- Works on any list.
- Time Complexity: O(n)

## Binary Search

- Requires a sorted list.
- Time Complexity: O(log n)

---

# Sorting Algorithms

## Bubble Sort

- Repeatedly swaps adjacent elements.
- Time Complexity: O(n²)

## Quick Sort

- Divide and Conquer
- Average: O(n log n)
- Worst: O(n²)

## Merge Sort

- Divide and Conquer
- Stable sorting algorithm
- Time Complexity: O(n log n)

---

# Recursion

A function calling itself until a base case is reached.

Key Concepts:

- Base Case
- Recursive Case

Examples implemented:

- Factorial
- Fibonacci
- Sum of Digits

---

# Key Takeaways

- Choose the appropriate data structure for the problem.
- Analyze both time and space complexity.
- Prefer O(log n) or O(n log n) algorithms when possible.
- Understand recursion before learning dynamic programming.
- Practice implementing data structures from scratch to strengthen problem-solving skills.