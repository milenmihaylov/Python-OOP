class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        for i in range(self.count, -1, -1):
            yield i


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
