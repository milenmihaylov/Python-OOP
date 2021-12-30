class Parent:
    _possible_drinks = ['beer', 'wine']


class Child(Parent):
    def __init__(self):
        self._possible_drinks = super()._possible_drinks + ['Vodka']

