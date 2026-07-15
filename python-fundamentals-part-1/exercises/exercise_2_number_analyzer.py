# ==========================================
# Exercise 2: Number Analyzer
# ==========================================


def is_even(number):
    return number % 2 == 0


def is_positive(number):
    return number >= 0


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def factorial(number):
    if number < 0:
        return None

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


number = int(input("Enter a number: "))

print("\n===== Number Analysis =====")

if is_positive(number):
    print("The number is Positive.")
else:
    print("The number is Negative.")

if is_even(number):
    print("The number is Even.")
else:
    print("The number is Odd.")

if is_prime(number):
    print("The number is Prime.")
else:
    print("The number is Not Prime.")

fact = factorial(number)

if fact is None:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial: {fact}")