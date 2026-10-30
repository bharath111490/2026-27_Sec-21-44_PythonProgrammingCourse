num = int(input("Enter a number: "))

print("Using for loop:")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("\nUsing while loop:")
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
