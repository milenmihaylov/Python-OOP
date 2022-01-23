class Player:
    __players_names = []
    stamina_max_value = 100
    __stamina_min_value = 0

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina
        # self.need_sustenance: bool = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0 and isinstance(value, str):
            raise ValueError("Name not valid!")
        if value in self.__players_names:
            raise Exception(f"Name {value} is already used!")
        self.__collect_name(value)
        self.__name = value

    @classmethod
    def __collect_name(cls, name):
        cls.__players_names.append(name)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if self.stamina_max_value < value < self.__stamina_min_value:
            raise ValueError("Stamina not valid!")
        self.__stamina = value
    
    @property
    def need_sustenance(self):
        if self.stamina < 100:
            return True
