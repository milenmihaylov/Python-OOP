def log(func):
    def wrapper():
        print(f"{func.__name__} executed")
        return func()

    return wrapper


@log
def f1():
    return 5


print(f1())
