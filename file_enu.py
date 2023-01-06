# enumerate
av = ['haw', 'iro', 'tho', 'qui']
e = enumerate(av)
print(type(e))

e_list = list(e)
print(e_list)

for index, value in enumerate(av):
    print(index, value)

nam = ['ba', 'st', 'od', 'ma']

z = zip(av, nam)
print(type(z))

z_list = list(z)

for z1, z2 in zip(av, nam):
    print(z1, z2)
