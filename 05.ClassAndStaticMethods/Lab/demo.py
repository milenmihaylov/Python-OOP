from demo_1 import create_id_generator


class Person:
    _min_name_length = 2
    _max_name_length = 15
    get_id = create_id_generator()

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = Person.get_id()

    @staticmethod
    def sample_static_method():
        print('This is independent from class')

    @staticmethod
    def validate_name(value):
        if Person._min_name_length > len(value) or len(value) > Person._max_name_length:
            raise ValueError("Name must be more than 2 cars")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.validate_name(value)
        self.__name = value


class Student(Person):
    _min_student_name_length = 3

    def __init__(self, name, age):
        super().__init__(name, age)

    # не трябва да предефинираме getters and setters
    @staticmethod
    def validate_name(value):
        Person.validate_name(value)
        if Student._min_student_name_length > len(value):
            raise ValueError('Name must be more than 3 char')


# new_student = Student('aaa', 6)
# print(new_student.name)
# Person('1u', 8)
# Student('1u', 9)

for i in range(5):
    print(Person('asd', 5).__dict__)
