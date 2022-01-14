class custom_range:
    def __init__(self, start: int, end: int, step: int = 1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return CustomRangeIterator(self)


class CustomRangeIterator:
    def __init__(self, cr: custom_range):
        self.start = cr.start
        self.end = cr.end
        self.step = cr.step
        self.current_number = self.start

    def __next__(self):
        if self.step > 0 and self.current_number > self.end:
            raise StopIteration
        if self.step < 0 and self.current_number < self.end:
            raise StopIteration

        value = self.current_number
        self.current_number += self.step
        return value


one_to_ten = custom_range(5, 1, -3)
for x in one_to_ten:
    print(x)
