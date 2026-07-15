# Object-Oriented Python & Advanced Features Notes

## Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects. An object contains data (attributes) and behavior (methods).

### Class

A class is a blueprint for creating objects.

```python
class Student:
    pass
```

### Object

An object is an instance of a class.

```python
student = Student()
```

---

## Constructor

The `__init__()` method initializes object attributes when an object is created.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

## Attributes

Attributes store information about an object.

```python
student.name
student.age
```

---

## Methods

Methods define the behavior of an object.

```python
def display(self):
    print(self.name)
```

---

# Inheritance

Inheritance allows one class to inherit properties and methods from another class.

```python
class Animal:
    pass

class Dog(Animal):
    pass
```

Benefits:

* Code reuse
* Better organization
* Easier maintenance

---

# Method Overriding

A child class can replace the implementation of a parent class method.

```python
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")
```

---

# super()

The `super()` function is used to call methods from the parent class.

```python
super().__init__(name)
```

---

# List Comprehensions

A concise way to create lists.

Traditional loop:

```python
squares = []

for i in range(5):
    squares.append(i * i)
```

List comprehension:

```python
squares = [i * i for i in range(5)]
```

Benefits:

* Cleaner
* Shorter
* More Pythonic

---

# Decorators

A decorator modifies the behavior of another function without changing its code.

```python
@logger
def greet():
    print("Hello")
```

Common uses:

* Logging
* Authentication
* Timing
* Validation

---

# Iterators

An iterator produces one value at a time.

Iterator methods:

* `__iter__()`
* `__next__()`

Example:

```python
for item in iterator:
    print(item)
```

---

# Generators

Generators produce values lazily using the `yield` keyword.

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Advantages:

* Memory efficient
* Suitable for large datasets
* Used extensively in AI and data processing

---

# Generator vs Iterator

| Generator        | Iterator                           |
| ---------------- | ---------------------------------- |
| Uses `yield`     | Uses `__iter__()` and `__next__()` |
| Easier to write  | More control                       |
| Memory efficient | Memory efficient                   |

---

# Key Takeaways

* Classes create reusable object templates.
* Objects contain attributes and methods.
* Inheritance promotes code reuse.
* Method overriding customizes inherited behavior.
* List comprehensions provide a cleaner alternative to loops.
* Decorators extend function behavior.
* Iterators return one value at a time.
* Generators simplify lazy iteration using `yield`.
