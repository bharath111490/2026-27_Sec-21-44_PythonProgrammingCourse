# Demonstrate continue statement using for loop and while loop

print("Using for loop:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print("\nUsing while loop:")
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)