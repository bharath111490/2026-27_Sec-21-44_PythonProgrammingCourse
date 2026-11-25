squares_dict = {num: num**2 for num in range(1, 11)}

print("Numbers and their Squares:")
for key, value in squares_dict.items():
    print(key, ":", value)