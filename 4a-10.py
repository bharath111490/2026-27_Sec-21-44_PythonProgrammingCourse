students = [
    {"name": "Ravi", "marks": 85},
    {"name": "Priya", "marks": 92},
    {"name": "Kiran", "marks": 78},
    {"name": "Anu", "marks": 88}
]

ascending = sorted(students, key=lambda x: x["marks"])
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("Ascending Order:")
for student in ascending:
    print(student)

print("\nDescending Order:")
for student in descending:
    print(student)
