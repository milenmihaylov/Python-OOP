ll = [1, 2, 3, 4]


def increment(x):
    return x + 1


print(map(increment, ll))


for x in map(increment, ll):
    print(x)
