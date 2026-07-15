# Concurrency — Multithreading & Multiprocessing

This repository is part of my **AI Engineer Dev Weekend Journey**.

The goal of this project is to understand Python's concurrency models and learn when to use sequential execution, multithreading, multiprocessing, and asyncio.

The project includes practical implementations, performance comparisons, and concise notes to build a strong foundation for future AI engineering tasks.

---

# Learning Objectives

- Understand concurrency and parallelism
- Learn the difference between threading and multiprocessing
- Understand the Global Interpreter Lock (GIL)
- Use `ThreadPoolExecutor` for I/O-bound tasks
- Use `ProcessPoolExecutor` for CPU-bound tasks
- Understand asynchronous programming using `asyncio`
- Compare execution times of different concurrency models

---

# Project Structure

```text
concurrency-multithreading-multiprocessing/
│
├── benchmark.py
├── notes.md
├── README.md
├── requirements.txt
├── urls.py
│
├── examples/
│   ├── __init__.py
│   ├── sequential_fetch.py
│   ├── threaded_fetch.py
│   ├── multiprocessing_demo.py
│   └── asyncio_demo.py
```

---

# Concepts Covered

## Sequential Execution

- One task at a time
- Simple execution model

---

## Multithreading

- ThreadPoolExecutor
- Parallel URL fetching
- I/O-bound tasks
- Shared memory
- GIL considerations

---

## Multiprocessing

- ProcessPoolExecutor
- CPU-bound computations
- Multiple processes
- True parallel execution

---

## Asyncio

- Event loop
- Coroutines
- async / await
- Lightweight concurrency

---

## Global Interpreter Lock (GIL)

- Why the GIL exists
- Effect on threading
- Why multiprocessing bypasses the GIL

---

# Requirements

Install the required package:

```bash
pip install -r requirements.txt
```

---

# How to Run

## Sequential Fetch

```bash
python -m examples.sequential_fetch
```

---

## Threaded Fetch

```bash
python -m examples.threaded_fetch
```

---

## Multiprocessing Demo

```bash
python -m examples.multiprocessing_demo
```

---

## Asyncio Demo

```bash
python -m examples.asyncio_demo
```

---

## Benchmark Summary

```bash
python benchmark.py
```

---

# Expected Learning Outcomes

After completing this project, I can:

- Explain concurrency vs parallelism
- Describe the Global Interpreter Lock (GIL)
- Identify I/O-bound and CPU-bound tasks
- Implement multithreading using `ThreadPoolExecutor`
- Implement multiprocessing using `ProcessPoolExecutor`
- Explain when to use `asyncio`
- Compare different concurrency models based on performance and use cases

---

# Acceptance Criteria

- ✅ Understand the difference between threading and multiprocessing
- ✅ Explain the Global Interpreter Lock (GIL)
- ✅ Implement parallel URL fetching using `ThreadPoolExecutor`
- ✅ Compare sequential and threaded execution
- ✅ Demonstrate multiprocessing for CPU-bound tasks
- ✅ Explain when to use threading, multiprocessing, and asyncio

---

# Key Takeaways

- Sequential execution is simple but slow for waiting tasks.
- Threading is ideal for I/O-bound workloads.
- Multiprocessing is ideal for CPU-bound workloads.
- Asyncio provides efficient concurrency using a single thread and an event loop.
- Choosing the correct concurrency model depends on the nature of the workload.

---

This repository serves as a practical introduction to Python concurrency and provides a foundation for building scalable AI and machine learning applications.