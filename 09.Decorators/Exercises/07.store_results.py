from functools import wraps


# class store_results:
#     def __init__(self, func):
#         self.func = func
#         self.file = open('results.txt', 'a')
#
#     def __call__(self, *args, **kwargs):
#         result = self.func(*args, **kwargs)
#         to_write = f"Function {self.func.__name__} was add called. Result: {str(result)}\n"
#         self.file.write(to_write)
#         self.file.close()


def store_results(func):
    @wraps(func)
    def wrapper(*args):
        file = open('results.txt', 'a')
        file.write(f"Function {func.__name__} was add called. Result: {func(*args)}\n")
        file.close()

    return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
