s = {1, 2, 2, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}

# print(type(s))
# print(s)

# s.add(6)
# print(s)

# s.remove(2)
# print(s)

# s.discard(2)
# print(s)

print(s.union(b))
print(s | b)

print(s.intersection(b))
print(s & b)

print(s.difference(b))
print(s - b)

print(s.symmetric_difference(b))
print(s ^ b)