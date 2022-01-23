import functools


def is_num(n):
    if isinstance(n, int):
        return True
    return False


def even_parameters(func):
    @functools.wraps(func)
    def wrapper(*args):
        for x in args:
            if not (is_num(x) and x % 2 == 0):
                return "Please use only even numbers!"
        return func(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
