import functools


def repeat(count):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(count):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


def say_hi():
    return 'Hi, Milen!'


@repeat(5)
def printer(x):
    print(x)


printer(say_hi())
