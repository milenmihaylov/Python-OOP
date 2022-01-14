class reverse_iter:
    def __init__(self, iter):
        self.iter = iter
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.__index) > len(self.iter):
            raise StopIteration

        value = self.iter[self.__index]
        self.__index -= 1
        return value


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
