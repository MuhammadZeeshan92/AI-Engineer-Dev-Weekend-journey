# ==========================================
# Functions in Python
# Regular Functions, Parameters, Return,
# Default Arguments, Keyword Arguments,
# *args, **kwargs, Lambda Functions
# ==========================================

print("\n========== Regular Function ==========\n")


def greet():
    print("Welcome to Python Fundamentals!")


greet()


print("\n========== Function with Parameters ==========\n")


def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Zeeshan")


print("\n========== Function with Return Value ==========\n")


def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)
print("Sum:", result)


print("\n========== Default Arguments ==========\n")


def introduce(name, country="Pakistan"):
    print(f"My name is {name} and I live in {country}.")


introduce("Zeeshan")
introduce("Ali", "Canada")


print("\n========== Keyword Arguments ==========\n")


def student_info(name, age, course):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")


student_info(course="AI Engineering", age=21, name="Zeeshan")


print("\n========== Variable-Length Arguments (*args) ==========\n")


def calculate_sum(*numbers):
    total = sum(numbers)
    print("Numbers:", numbers)
    print("Sum:", total)


calculate_sum(10, 20)
calculate_sum(5, 10, 15, 20)


print("\n========== Keyword Variable-Length Arguments (**kwargs) ==========\n")


def display_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


display_profile(
    name="Zeeshan",
    age=21,
    university="UMT",
    field="AI Engineering"
)


print("\n========== Lambda Functions ==========\n")

square = lambda x: x ** 2
print("Square of 5:", square(5))

multiply = lambda a, b: a * b
print("Multiplication:", multiply(6, 7))


print("\n========== Using Lambda with map() ==========\n")

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print("Original Numbers:", numbers)
print("Squared Numbers:", squares)


print("\n========== Using Lambda with filter() ==========\n")

numbers = [10, 15, 20, 25, 30]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original Numbers:", numbers)
print("Even Numbers:", even_numbers)


print("\n========== Practical Example ==========\n")


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"


student_marks = 86

print(f"Marks: {student_marks}")
print(f"Grade: {calculate_grade(student_marks)}")