# Concurrency — Notes

## What is Concurrency?

Concurrency is the ability of a program to make progress on multiple tasks during the same period of time.

Concurrency improves performance for tasks that spend time waiting, such as network requests or file operations.

---

# Concurrency Models

## 1. Sequential Execution

- Executes one task at a time.
- Simple but slow for I/O-bound workloads.

Example:

Task 1 → Task 2 → Task 3

---

## 2. Multithreading

- Uses multiple threads within the same process.
- Threads share the same memory.
- Best for I/O-bound tasks.

Examples:
- API requests
- Web scraping
- Downloading files
- Reading files
- Database queries

Python Tool:
- ThreadPoolExecutor

---

## 3. Multiprocessing

- Uses multiple processes.
- Each process has its own Python interpreter and memory.
- Not limited by the GIL.
- Best for CPU-bound tasks.

Examples:
- Image processing
- Machine Learning preprocessing
- Numerical computation
- Video processing

Python Tool:
- ProcessPoolExecutor

---

## 4. Asyncio

- Uses a single thread with an event loop.
- No additional threads are created.
- Uses async and await.
- Best for handling many waiting tasks efficiently.

Examples:
- FastAPI
- Async database clients
- High-performance web servers

---

# The Global Interpreter Lock (GIL)

The Global Interpreter Lock (GIL) allows only one thread to execute Python bytecode at a time within a process.

Effects:
- Limits parallel execution of CPU-bound threads.
- Does not significantly affect I/O-bound tasks because threads release the GIL while waiting.

---

# Threading vs Multiprocessing vs Asyncio

| Feature | Threading | Multiprocessing | Asyncio |
|----------|-----------|-----------------|----------|
| Multiple Threads | Yes | No | No |
| Multiple Processes | No | Yes | No |
| Single Thread | No | No | Yes |
| Best for I/O | Yes | No | Yes |
| Best for CPU | No | Yes | No |
| Uses async/await | No | No | Yes |
| Affected by GIL | Yes | No | Yes |

---

# ThreadPoolExecutor

Used to execute I/O-bound tasks concurrently.

Common Methods:

- submit()
- map()

Useful with:
- requests
- file operations
- network calls

---

# ProcessPoolExecutor

Used to execute CPU-intensive tasks in parallel across multiple CPU cores.

Suitable for:
- Large calculations
- Data preprocessing
- Image processing

---

# async / await

async:
- Declares an asynchronous function.

await:
- Pauses the current coroutine until the awaited operation completes while allowing other coroutines to run.

---

# Event Loop

The event loop schedules and executes asynchronous tasks.

It switches between coroutines whenever one is waiting.

---

# When to Use What?

Use Sequential when:
- Simplicity is more important than speed.

Use Threading when:
- Waiting for network or disk operations.

Use Multiprocessing when:
- Heavy CPU computations are involved.

Use Asyncio when:
- Managing thousands of concurrent I/O operations.

---

# Project Summary

Implemented:

- Sequential URL fetching
- Parallel URL fetching using ThreadPoolExecutor
- CPU-bound multiprocessing example
- Asyncio demonstration

Compared execution times to understand the strengths of each concurrency model.

---

# Key Takeaways

- Concurrency is not the same as parallelism.
- Threading is ideal for I/O-bound tasks.
- Multiprocessing is ideal for CPU-bound tasks.
- Asyncio provides lightweight concurrency using a single thread.
- The GIL limits CPU-bound threading but has little impact on I/O-bound workloads.