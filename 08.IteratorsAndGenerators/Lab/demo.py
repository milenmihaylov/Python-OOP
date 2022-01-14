class Person:
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        return PersonIterator(self)


class PersonIterator:
    def __init__(self, person: Person):
        self.person = person
        self.__index = 0

    def __next__(self):
        if self.__index == len(self.person.name):
            raise StopIteration

        value = self.person.name[self.__index]
        self.__index += 1
        return value


ll = [1, 2, 3, 4, 5]
gosho = Person('Gosho')
ll_iter1 = iter(gosho)
ll_iter2 = iter(gosho)

print(type(ll_iter1))
print(ll_iter1)

print(next(ll_iter2))
print(next(ll_iter1))
print(next(ll_iter1))
print(next(ll_iter2))
print(next(ll_iter2))
#
print(next(ll_iter1))
