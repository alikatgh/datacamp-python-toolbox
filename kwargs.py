def s(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(s(5, 5, 5, 5, 5, 5))


def s(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)

print(s(i=5, l=5, q=5.4334))