subject_marks = {
    "Maths": 95,
    "Science": 88,  
    "English": 90,
    "Computer": 98
}

print("Keys:")
for key in subject_marks.keys():
    print(key)

print("\nValues:")
for value in subject_marks.values():
    print(value)

print("\nItems:")
for key, value in subject_marks.items():
    print(key, ":", value)