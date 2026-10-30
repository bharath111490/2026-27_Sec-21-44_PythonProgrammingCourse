# Print numbers from 1 to N using for loop and while loop

n = int(input("Enter N: "))

print("Using for loop:")
for i in range(1, n + 1):
    print(i)

print("Using while loop:")
i = 1
while i <= n:
    print(i)
    i += 1
