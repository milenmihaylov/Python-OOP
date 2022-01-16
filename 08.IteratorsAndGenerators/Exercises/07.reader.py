def read_next(*args):
    for x in args:
        for c in x:
            yield c


for item in read_next("string", (2,), {"d": 1, "I": 2, "c": 3, "t": 4}):
    print(item, end='')

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)