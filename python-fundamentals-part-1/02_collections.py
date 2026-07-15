# ==========================================
# Collections in Python
# Lists, Tuples, Sets, and Dictionaries
# ==========================================

print("\n========== Lists ==========\n")

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original List:", fruits)

print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

print("Slicing (First 2):", fruits[:2])

fruits.append("Grapes")
print("After Append:", fruits)

fruits.insert(1, "Kiwi")
print("After Insert:", fruits)

fruits.remove("Banana")
print("After Remove:", fruits)

removed_item = fruits.pop()
print("Popped Item:", removed_item)
print("After Pop:", fruits)

fruits.sort()
print("Sorted List:", fruits)

fruits.reverse()
print("Reversed List:", fruits)

print("Length:", len(fruits))


print("\n========== Tuples ==========\n")

colors = ("Red", "Green", "Blue", "Yellow")

print("Tuple:", colors)
print("First Color:", colors[0])
print("Last Color:", colors[-1])
print("Slicing:", colors[1:3])
print("Length:", len(colors))

print("Tuples are immutable, so their values cannot be changed.")


print("\n========== Sets ==========\n")

numbers = {1, 2, 3, 4, 5}
print("Original Set:", numbers)

numbers.add(6)
print("After Add:", numbers)

numbers.remove(2)
print("After Remove:", numbers)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Set A:", set_a)
print("Set B:", set_b)

print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference (A - B):", set_a.difference(set_b))


print("\n========== Dictionaries ==========\n")

student = {
    "name": "Zeeshan",
    "age": 21,
    "course": "AI Engineering"
}

print("Original Dictionary:")
print(student)

print("Name:", student["name"])
print("Age:", student["age"])

student["age"] = 22
print("Updated Age:", student)

student["city"] = "Lahore"
print("After Adding City:")
print(student)

del student["course"]
print("After Deleting Course:")
print(student)

print("\nDictionary Keys:")
for key in student.keys():
    print(key)

print("\nDictionary Values:")
for value in student.values():
    print(value)

print("\nDictionary Key-Value Pairs:")
for key, value in student.items():
    print(f"{key}: {value}")