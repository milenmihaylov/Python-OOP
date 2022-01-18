def number_increment(numbers: list):
    def increase(n):
        return [x + n for x in numbers]

    return increase


def func():
    pass


n1 = number_increment([1, 2, 3])
print(number_increment)
print(n1(2))
print(func)
