class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current_number = 0
        self.cnt = self.count

    # def __iter__(self):
    #     end = self.count * self.step
    #     for i in range(0, end, self.step):
    #         yield i

    def __iter__(self):
        return self

    def __next__(self):
        if self.cnt == 0:
            raise StopIteration

        if self.cnt < self.count:
            self.current_number += self.step
        value = self.current_number
        self.cnt -= 1
        return value


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
