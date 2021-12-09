class Person:
    def __init__(self, name, age):
        self.name = name
        self.get_age = age

    @property
    def age(self):
        return

    @age.setter
    def age(self, value):
        pass


p = Person('Stive O', 25)
print(type(p.__class__.__name__))
