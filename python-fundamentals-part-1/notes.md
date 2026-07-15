# Python Fundamentals – Part 1 Notes

## Variables

A variable is used to store data in memory.

```python
name = "Zeeshan"
age = 21
```

### Variable Naming Rules

* Must start with a letter or underscore (`_`)
* Cannot start with a number
* Case-sensitive (`age` and `Age` are different)
* Use meaningful names

---

## Data Types

### Integer (`int`)

Whole numbers.

```python
age = 21
```

### Float (`float`)

Decimal numbers.

```python
height = 5.9
```

### String (`str`)

Text enclosed in single or double quotes.

```python
name = "Python"
```

### Boolean (`bool`)

Represents `True` or `False`.

```python
is_student = True
```

### Check Data Type

```python
print(type(name))
```

---

## Type Casting

Convert one data type into another.

```python
int("10")
float(5)
str(100)
bool(1)
```

---

## Operators

### Arithmetic Operators

* `+` Addition
* `-` Subtraction
* `*` Multiplication
* `/` Division
* `//` Floor Division
* `%` Modulus
* `**` Exponent

### Comparison Operators

* `==`
* `!=`
* `>`
* `<`
* `>=`
* `<=`

### Assignment Operators

* `=`
* `+=`
* `-=`
* `*=`
* `/=`

---

## User Input

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
```

---

## f-Strings

Used to format strings.

```python
print(f"My name is {name}")
```

---

# Collections

## List

Ordered and mutable.

```python
fruits = ["Apple", "Banana", "Mango"]
```

Common Methods

* `append()`
* `insert()`
* `remove()`
* `pop()`
* `sort()`
* `reverse()`

---

## Tuple

Ordered and immutable.

```python
colors = ("Red", "Green", "Blue")
```

---

## Set

Unordered collection of unique values.

```python
numbers = {1, 2, 3}
```

Common Methods

* `add()`
* `remove()`
* `union()`
* `intersection()`

---

## Dictionary

Stores data as key-value pairs.

```python
student = {
    "name": "Zeeshan",
    "age": 21
}
```

Common Methods

* `keys()`
* `values()`
* `items()`

---

# Control Flow

## if

```python
if age >= 18:
    print("Eligible")
```

## if-else

```python
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## if-elif-else

Used for multiple conditions.

---

## Loops

### for Loop

```python
for fruit in fruits:
    print(fruit)
```

### while Loop

```python
while count <= 5:
    count += 1
```

### break

Terminates the loop.

### continue

Skips the current iteration.

---

# Functions

## Regular Function

```python
def greet():
    print("Hello")
```

## Function with Parameters

```python
def greet(name):
    print(name)
```

## Return Statement

```python
def add(a, b):
    return a + b
```

## Default Arguments

```python
def introduce(name, country="Pakistan"):
    pass
```

## Keyword Arguments

```python
student(age=21, name="Ali")
```

## *args

Accepts multiple positional arguments.

```python
def total(*numbers):
    pass
```

## **kwargs

Accepts multiple keyword arguments.

```python
def profile(**details):
    pass
```

## Lambda Function

Anonymous one-line function.

```python
square = lambda x: x ** 2
```

---

# Key Takeaways

* Variables store data.
* Python has four common primitive data types: `int`, `float`, `str`, and `bool`.
* Lists, tuples, sets, and dictionaries are the primary collection types.
* Control flow is implemented using conditions and loops.
* Functions make code reusable and modular.
* Lambda functions provide a concise way to create simple anonymous functions.