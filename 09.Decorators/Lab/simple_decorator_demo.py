def uppercase(func_to_be_decorated):
    def wrapper():
        result = func_to_be_decorated()
        return str(result).upper()

    return wrapper


@uppercase
def say_hi():
    return 'Hello, Milen!'


print(say_hi())
