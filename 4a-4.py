students = {
    "101": {"name": "Ravi", "marks": 85},
    "102": {"name": "Priya", "marks": 92},
    "103": {"name": "Kiran", "marks": 78}
}

print("Student Details:")
for roll, details in students.items():
    print("Roll No:", roll)
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print()