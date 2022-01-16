from time import time


def fibonacci():
    x = 0
    y = 1
    yield x
    while True:
        x, y = y, x + y
        yield x


start = time()

generator = fibonacci()
for i in range(25550):
    print(next(generator))

end = time()
print(end - start)
