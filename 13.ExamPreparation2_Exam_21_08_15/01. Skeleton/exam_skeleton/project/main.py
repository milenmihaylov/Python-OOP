from project.bakery import Bakery

b = Bakery("Jorp")
print(b.name)
print(b.add_table("InsideTable", 31, 3))
print(b.add_table("OutsideTable", 51, 5))

print(b.reserve_table(10))

print(b.add_drink('Tea', 'Mint', 1, 'Lipton'))
print(b.add_drink('Water', 'Mneralna', 200, 'Devin'))
print(b.add_food('Cake', '6okolad', 5.90))
print(b.add_food('Bread', 'Dobridja', 5.90))
print(b.food_menu)
print(b.drinks_menu)
print(b.order_food(51, '6okolad'))
print(b.order_food(31, 'asdasd'))
print(b.order_drink(31, 'Mint', "Mneralna"))
print(b.order_drink(51, 'Mint', "Mneralna"))
print(b.get_free_tables_info())
