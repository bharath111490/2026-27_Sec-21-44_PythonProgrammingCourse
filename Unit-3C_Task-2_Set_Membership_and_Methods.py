s = {10, 20, 30}
# Membership testing
if 20 in s:
    print("20 is present in the set")
else:
    print("20 is not present in the set")
# Add element
s.add(40)
print("After add:", s)
# Remove element
s.remove(10)
print("After remove:", s)
# Discard element
s.discard(50)
print("After discard:", s)
