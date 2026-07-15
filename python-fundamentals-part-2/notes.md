# Python Fundamentals – Part 2 Notes

## Modules

A module is a Python file (`.py`) that contains functions, classes, or variables which can be imported into another Python file.

Example:

```python
from file_processor import read_file
```

Benefits:

* Reusable code
* Better organization
* Easier maintenance

---

## Imports

Python provides different ways to import modules.

Import the whole module:

```python
import math
```

Import specific functions:

```python
from math import sqrt
```

Import with an alias:

```python
import numpy as np
```

---

## Project Structure

A well-structured project separates responsibilities into different files.

Example:

```text
project/
│
├── main.py
├── utils.py
├── file_processor.py
├── input.txt
├── output.txt
├── requirements.txt
└── README.md
```

Benefits:

* Easy to understand
* Easy to maintain
* Reusable modules

---

## File Input and Output (File I/O)

Reading a file:

```python
with open("input.txt", "r") as file:
    content = file.read()
```

Writing to a file:

```python
with open("output.txt", "w") as file:
    file.write(content)
```

Using the `with` statement automatically closes the file after use.

---

## Exception Handling

Exceptions prevent programs from crashing unexpectedly.

Basic syntax:

```python
try:
    # Code that may cause an error
except:
    # Handle the error
finally:
    # Always executes
```

Common Exceptions:

* `FileNotFoundError`
* `PermissionError`
* `ValueError`
* `TypeError`
* `ZeroDivisionError`

---

## finally Block

The `finally` block always executes whether an exception occurs or not.

Example:

```python
try:
    print("Processing...")
finally:
    print("Finished")
```

---

## Third-Party Packages

Python packages provide additional functionality beyond the standard library.

Example package:

* `requests`

Installation:

```bash
pip install requests
```

or

```bash
pip install -r requirements.txt
```

Import:

```python
import requests
```

---

## requirements.txt

A `requirements.txt` file stores project dependencies.

Example:

```text
requests
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## CLI (Command Line Interface)

A CLI application is executed from the terminal.

Example:

```bash
python main.py
```

The user interacts with the program through terminal input and output.

---

# Key Takeaways

* Modules help organize and reuse code.
* Imports allow one file to use code from another.
* File I/O enables reading from and writing to files.
* Exception handling makes programs more reliable.
* Third-party packages extend Python's capabilities.
* `requirements.txt` helps manage project dependencies.
* A clear project structure improves readability and maintainability.
