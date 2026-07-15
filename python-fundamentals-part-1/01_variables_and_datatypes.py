# ==========================================
# Variables and Data Types
# ==========================================

print("\n========== Variables ==========\n")

name = "Zeeshan"
age = 21
height = 5.9
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)


print("\n========== Data Types ==========\n")

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


print("\n========== Type Casting ==========\n")

number_string = "100"
number = int(number_string)
print("String to Integer:", number)

price = 250
price_string = str(price)
print("Integer to String:", price_string)

height = 5.9
whole_height = int(height)
print("Float to Integer:", whole_height)

marks = 95
marks_float = float(marks)
print("Integer to Float:", marks_float)


print("\n========== Arithmetic Operators ==========\n")

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


print("\n========== Comparison Operators ==========\n")

print("10 > 5:", 10 > 5)
print("10 < 5:", 10 < 5)
print("10 == 5:", 10 == 5)
print("10 != 5:", 10 != 5)
print("10 >= 5:", 10 >= 5)
print("10 <= 5:", 10 <= 5)


print("\n========== Assignment Operators ==========\n")

x = 10
print("Initial Value:", x)

x += 5
print("After += 5:", x)

x -= 3
print("After -= 3:", x)

x *= 2
print("After *= 2:", x)

x /= 4
print("After /= 4:", x)

x %= 3
print("After %= 3:", x)


print("\n========== User Input ==========\n")

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(f"Hello {user_name}! You are {user_age} years old.")


print("\n========== f-Strings ==========\n")

language = "Python"

print(f"My name is {user_name}.")
print(f"I am learning {language}.")
print(f"Next year I will be {user_age + 1} years old.")