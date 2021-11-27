ll = sorted(list(range(1, 11)))
ll_2 = [x ** 2 for x in ll]


def sum_func(ll: list):
    result = 0
    for el in ll:
        result += el
    return result


class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return


#
# gosho = Person('Gosho', 20, 180)
# print(gosho)


class Student(Person):
    def __init__(self, name, age, height, ave_score=None):
        super().__init__(name, age, height)
        self.ave_score = ave_score


def my_func(a: int, ll: list):
    for i in range(len(ll)):
        first_num = ll[i]
        for j in range(len(ll)):
            if i == j:
                continue
            second_num = ll[j]
            if first_num + second_num == a:
                return True
    return False
