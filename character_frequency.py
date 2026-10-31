s = input("Enter a string: ")

for ch in s:
    count = s.count(ch)
    print(ch, "=", count)