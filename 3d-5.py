def find_sum(*args):
    total = 0
    for num in args:
        total += num
    return total
result1 = find_sum(10, 20, 30)
result2 = find_sum(5, 15, 25, 35)
print("Sum of first set:", result1)
print("Sum of second set:", result2)