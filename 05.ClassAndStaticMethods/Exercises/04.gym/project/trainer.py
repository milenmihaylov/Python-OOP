class Trainer:
    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        x = 0

        def get_id():
            nonlocal x
            x += 1
            return x

        return get_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
    