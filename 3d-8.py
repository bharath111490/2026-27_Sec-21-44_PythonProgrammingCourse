def student_details(**kwargs):
    print("Student Details:")
    for key, value in kwargs.items():
        print(key, ":", value)
student_details(
    name="Krishna",
    Maths=85,
    Science=90,
    English=88
)