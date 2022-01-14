class vowels:
    __vowels = 'aeiouy'

    def __init__(self, string: str):
        self.string = string
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.__is_in_range(self.__index, self.string):
            raise StopIteration
        while True:
            value = self.string[self.__index]
            self.__index += 1
            if value.lower() in self.__vowels:
                return value
            if not self.__is_in_range(self.__index, self.string):
                raise StopIteration

    @staticmethod
    def __is_in_range(i, word):
        if i >= len(word):
            return False
        return True


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
    for ch in my_string:
        print(ch)
