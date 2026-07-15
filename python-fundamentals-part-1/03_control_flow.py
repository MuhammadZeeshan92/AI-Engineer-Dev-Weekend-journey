# ==========================================
# Control Flow in Python
# if, elif, else, loops, break, continue
# ==========================================

print("\n========== if Statement ==========\n")

age = 20

if age >= 18:
    print("You are eligible to vote.")


print("\n========== if-else Statement ==========\n")

number = 7

if number % 2 == 0:
    print(f"{number} is Even.")
else:
    print(f"{number} is Odd.")


print("\n========== if-elif-else Statement ==========\n")

marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)


print("\n========== Nested if ==========\n")

age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Access Granted.")
    else:
        print("ID Card Required.")
else:
    print("Access Denied.")


print("\n========== for Loop ==========\n")

fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)


print("\n========== range() Function ==========\n")

print("Numbers from 1 to 5:")

for number in range(1, 6):
    print(number)


print("\n========== while Loop ==========\n")

count = 1

while count <= 5:
    print(count)
    count += 1


print("\n========== break Statement ==========\n")

for number in range(1, 11):
    if number == 6:
        print("Loop stopped at", number)
        break
    print(number)


print("\n========== continue Statement ==========\n")

for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)


print("\n========== Loop with else ==========\n")

for number in range(1, 6):
    print(number)
else:
    print("Loop completed successfully.")


print("\n========== Practical Example ==========\n")

numbers = [12, 7, 19, 4, 25]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")