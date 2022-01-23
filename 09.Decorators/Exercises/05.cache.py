import functools


def cache(func):
    log = {}

    @functools.wraps(func)
    def wrapper(x):
        if x not in log:
            log[x] = func(x)
        return log[x]
    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
