list_one = [1, 2, 3, 4, 5, 6]
list_two = ['a', 'b', 'c', 'd', 'f', 'e', 'g']
list_three = [1, 2, 3, 'd', 'f', 'e']

# list_four = [1], [1], [1], [1], [1]
 
print(list_one)
print(list_one, sep='')

list_one.insert(len(list_one), 5)
print(list_one)

list_one.append(6)
print(list_one)

list_final = [list_one, list_two, list_three]

list_doubled = list_final * 2
# list_one.extend([6, 7, 8, 9])
list_one.extend(list_final)
print(list_one)