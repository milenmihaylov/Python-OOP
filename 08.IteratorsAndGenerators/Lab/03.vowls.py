class vowels:
    def __init__(self, string: str):
        self.string = string

    def __iter__(self):
        return VowelsIterator(self)


class VowelsIterator:
    __vowels = 'aeiouy'

    def __init__(self, string: vowels):
        self.string = string.string
        self.index = 0

    def __next__(self):
        if not self.__is_in_range(self.index, self.string):
            raise StopIteration
        while True:
            value = self.string[self.index]
            self.index += 1
            if value.lower() in self.__vowels:
                return value
            if not self.__is_in_range(self.index, self.string):
                raise StopIteration

    @staticmethod
    def __is_in_range(i, word):
        if i >= len(word):
            return False
        return True


my_string = vowels('Abcedifuty0o')
my_name = vowels('Milen Iihaylov')
for char in my_name:
    print(char)
