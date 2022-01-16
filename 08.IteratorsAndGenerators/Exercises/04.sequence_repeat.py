from collections import deque


class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = deque(sequence)
        self.number = number
        self.__count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__count == self.number:
            raise StopIteration

        ch = self.sequence.popleft()
        self.sequence.append(ch)
        self.__count += 1
        return ch

    # def __iter__(self):
    #     for _ in range(self.number):
    #         ch = self.sequence.popleft()
    #         self.sequence.append(ch)
    #         yield ch


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
print()
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
