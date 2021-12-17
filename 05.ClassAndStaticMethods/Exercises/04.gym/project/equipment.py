class Equipment:
    __eq_id = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    @classmethod
    def get_next_id(cls):
        cls.__eq_id += 1
        return cls.__eq_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

