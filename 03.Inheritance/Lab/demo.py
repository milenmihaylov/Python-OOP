class Person:
    age = 21

    def __init__(self, name):
        self.name = name
        self.hobbies = set()
        """и ако това решиш да го направиш е сет, 
        тогава на всяка инстанция трябва да ходиш и преправяш метода"""

    def add_hobby(self, hobby):
        # тук можеш да направиш всякакви проверки
        self.hobbies.add(hobby)

    def __str__(self):
        if not self.hobbies:
            return f"{self.name} has no hobbies"
        return f"{self.name} has hobbies {self.hobbies}"


class MiddlePerson(Person):
    pass


class SoftwareDeveloper(Person):
    def __init__(self, name):
        super().__init__(name)
        self.add_hobby('Lego')
        self.add_hobby('Racing')


class Teacher(MiddlePerson):
    def __init__(self, name):
        super().__init__(name)
        self.subject = []

    def add_subject(self, subject):
        self.subject.append(subject)
        self.add_hobby(subject)

    def __str__(self):
        super_str = super().__str__()
        if self.subject:
            subjects = f' and subjects: {self.subject}'
        else:
            subjects = f' and no subjects'
        return super_str + subjects


mr_george = Teacher('Mr.George')
gosho = SoftwareDeveloper('Gosho')
mr_george.add_subject('Math')
print(mr_george)
print(gosho)

# pesho = SoftwareDeveloper('Pesho')
# gosho = Person('Gosho')
# # pesho.hobbies.append('Baking')  # НЕ СЕ ПРАВИ ТАКА. НАРУШАВАШ КОНЦЕПЦИЯТА НА ЕНКАПСУЛАЦИЯТА
#
# pesho.add_hobby('hiking')  # това е правилния начин
# print(pesho)  # SoftwareDeveloper няма __str__, наследява го от Person
# print(pesho.age)
# print(gosho.age)
