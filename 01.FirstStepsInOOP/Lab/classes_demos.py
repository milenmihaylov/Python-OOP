class Phone:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.color} {self.size} turned on!")


p1 = Phone("green", 4.6)
p2 = Phone(size=5.2, color='red')

p1.turn_on()
p2.turn_on()
