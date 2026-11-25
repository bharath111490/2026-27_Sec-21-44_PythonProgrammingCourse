student = {
    "name": "Krishna",
    "age": 20,
    "course": "Python"
}
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Name:", student.get("name"))
student.update({"age": 21, "city": "Guntur"})
print("After update:", student)
student.pop("course")
print("After pop:", student)