# ==========================================
# Exercise 1: Student Grade Manager
# ==========================================

student = {}

student["name"] = input("Enter student name: ")

marks = []

for subject in range(1, 4):
    mark = float(input(f"Enter marks for Subject {subject}: "))
    marks.append(mark)

average = sum(marks) / len(marks)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

student["marks"] = marks
student["average"] = average
student["grade"] = grade

print("\n===== Student Report =====")
print(f"Name: {student['name']}")
print(f"Marks: {student['marks']}")
print(f"Average: {student['average']:.2f}")
print(f"Grade: {student['grade']}")