class Laptop:
    brand = "Dell"

    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return f'This is brand {self.brand} laptop'

    def __repr__(self):
        return f'This is brand {self.brand} laptop2222'


l1 = Laptop('Latitude 5000')
l2 = Laptop('Latitude 5000')
l3 = l1
print(l1.name)
print(l3.name)
l1.name = 'new valid_name'
# Laptop.brand = 'HP'

print(l1 == l2)
print(l1.name == l2.name)
print(l2.brand)
print(l3 == l1)
print(l1.name)
print(l3.name)
print(l1)
