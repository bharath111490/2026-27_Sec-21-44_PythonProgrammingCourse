def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si
interest1 = simple_interest(10000, 2)
print("Simple Interest using default rate =", interest1)
interest2 = simple_interest(10000, 2, 8)
print("Simple Interest using explicit rate =", interest2)