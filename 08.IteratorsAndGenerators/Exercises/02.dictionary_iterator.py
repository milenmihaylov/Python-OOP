class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.__keys = list(self.dictionary.keys())
        self.__end = len(self.__keys)
        self.__start = 0

    # def __iter__(self):
    #     for tup in self.dictionary.items():
    #         yield tup

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start == self.__end:
            raise StopIteration

        key = self.__keys[self.__start]
        value = self.dictionary[key]
        self.__start += 1
        return key, value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
