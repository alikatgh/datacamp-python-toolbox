d = {1: 'C', 2: 'B', 3: 'G'}

# print(d)
# print(d[1])

# d[1] = 'Y'
# print(d[1])

# del d[1]
# print(d)

d2 = {}
print(type(d2))

d2 = 'Three'
print(d2)

d2 = 4
print(d2)

# del d2
print(d2)

for x in d2:
    print(x)


for key, value in d.items():
    print(str(key) + ' : ' + value)