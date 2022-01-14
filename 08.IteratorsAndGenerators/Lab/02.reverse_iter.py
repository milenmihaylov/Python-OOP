class reverse_iter:
    def __init__(self, iter):
        self.iter = iter

    def __iter__(self):
        return reverse_iter_iterator(self)


class reverse_iter_iterator:
    def __init__(self, iter: reverse_iter):
        self.iter = iter.iter
        self.index = -1

    def __next__(self):
        if abs(self.index) > len(self.iter):
            raise StopIteration

        value = self.iter[self.index]
        self.index -= 1
        return value


reversed_list = reverse_iter()
for item in reversed_list:
    print(item)
