from EXAM_Retake_21_12_20.first_try.project import Controller
from EXAM_Retake_21_12_20.first_try.project import Player
from EXAM_Retake_21_12_20.first_try.project import Drink
from EXAM_Retake_21_12_20.first_try.project import Food

controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player))
print(controller.duel("Peter", "Lilly"))
print(controller.add_player(first_player))
print(controller.sustain("Lilly", "Drink"))
first_player.stamina = 0
print(controller.duel("Peter", "Lilly"))
controller.next_day()
print(first_player.stamina)
print(second_player.stamina)