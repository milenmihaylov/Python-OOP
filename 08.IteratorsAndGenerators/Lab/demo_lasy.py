def fibonacci(n):
    fib = [0, 1]
    for _ in range(n):
        fib.append(fib[-1] + fib[-2])
    return fib


def fibonacci_gen():
    x = 0
    y = 1
    yield x
    while True:
        x, y = y, x + y
        yield x


print(fibonacci(10))
print(type(fibonacci_gen()))

fibonacci_iter = fibonacci_gen()
for i in range(5):
    print(next(fibonacci_iter))

for i in range(10):
    print(next(fibonacci_iter))
