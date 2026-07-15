# Python Fundamentals – Part 2

This repository is part of my **AI Engineer Dev Weekend Journey**, focusing on writing Python programs with a modular structure, handling files, managing exceptions, and working with third-party packages.

## Objective

The goal of this project is to understand how real-world Python projects are organized by using modules, file handling, exception handling, and package management.

## Topics Covered

* Modules
* Imports
* Project Structure
* File Input and Output (File I/O)
* Exception Handling
* `try`, `except`, `finally`
* Third-Party Packages
* `pip`
* `requirements.txt`
* Command Line Interface (CLI)

## Project Structure

```text
python-fundamentals-part-2/
│
├── README.md
├── notes.md
├── requirements.txt
│
├── main.py
├── file_processor.py
├── utils.py
├── sample_package_demo.py
│
├── input.txt
├── output.txt
```

## Features

* Reads data from an input file.
* Processes the file contents by converting text to uppercase.
* Counts the number of lines, words, and characters.
* Writes the processed content and statistics to an output file.
* Handles common file-related exceptions gracefully.
* Demonstrates the use of a third-party package (`requests`).

## Installation

Clone the repository and install the required package:

```bash
pip install -r requirements.txt
```

## How to Run

Run the main application:

```bash
python main.py
```

Run the third-party package example:

```bash
python sample_package_demo.py
```

## Expected Output

After running `main.py`, the program generates an `output.txt` file containing:

* Processed (uppercase) text
* Total number of lines
* Total number of words
* Total number of characters

## Learning Outcomes

After completing this project, I can:

* Organize Python code into multiple modules.
* Import functions from other files.
* Read and write files using Python.
* Handle exceptions using `try`, `except`, and `finally`.
* Install and use third-party packages with `pip`.
* Build a simple command-line application.

## Author

**Zeeshan Zakir**

This project is part of my journey toward becoming an AI Engineer.
