from typing import List
from player import Player
from supply.drink import Drink
from supply.food import Food
from supply.supply import Supply


class Controller:
    players: List[Player] = []
    supplies: List[Supply] = []

    def __init__(self):
        pass

    @classmethod
    def add_player(cls, *args: Player):
        added_new_players = []
        for player in args:
            if player not in cls.players:
                cls.players.append(player)
                added_new_players.append(player)
        return f"Successfully added: {', '.join(x.name for x in added_new_players)}"

    @classmethod
    def add_supply(cls, *args):
        cls.supplies.extend(list(args))

    @classmethod
    def sustain(cls, player_name: str, sustenance_type: str):
        if sustenance_type == 'Food' or sustenance_type == 'Drink':
            for player in cls.players:
                if player.name == player_name:
                    if not cls.__player_needs_supply(player):
                        return f"{player_name} have enough stamina."
                    if sustenance_type == 'Food' and not cls.__has_food():
                        raise Exception("There are no food supplies left!")
                    if sustenance_type == 'Drink' and not cls.__has_drink():
                        raise Exception("There are no drink supplies left!")
                    needed_supply = cls.__find_last_supply(sustenance_type)
                    cls.__heal_player(player, needed_supply)
                    return f"{player_name} sustained successfully with {needed_supply.name}."

    @classmethod
    def __find_last_supply(cls, sustenance_type):
        if sustenance_type == 'Food':
            for i in range(len(cls.supplies) - 1, -1, -1):
                if cls.supplies[i].__class__.__name__ == 'Food':
                    # if isinstance(cls.supplies[i], Food):
                    return cls.supplies.pop(i)
        elif sustenance_type == 'Drink':
            for i in range(len(cls.supplies) - 1, -1, -1):
                if cls.supplies[i].__class__.__name__ == 'Drink':
                    # if isinstance(cls.supplies[i], Drink):
                    return cls.supplies.pop(i)

    @staticmethod
    def __heal_player(player, supply):
        total_stamina = player.stamina + supply.valid_energy
        if total_stamina > Player.stamina_max_value:
            total_stamina = Player.stamina_max_value
        player.stamina = total_stamina

    @classmethod
    def __has_drink(cls):
        for supply in cls.supplies:
            if supply.__class__.__name__ == 'Drink':
                return True
        return False

    @classmethod
    def __has_food(cls):
        for supply in cls.supplies:
            if supply.__class__.__name__ == 'Food':
                return True
        return False

    @staticmethod
    def __player_needs_supply(player: Player):
        if player.stamina < Player.stamina_max_value:
            return True

    @classmethod
    def duel(cls, first_player_name: str, second_player_name: str):
        first_player, second_player = cls.__find_players(first_player_name, second_player_name)
        if first_player.stamina <= 0 and second_player.stamina <= 0:
            return f"Player {first_player.name} does not have enough stamina.\n" \
                   f"Player {second_player.name} does not have enough stamina."
        elif first_player.stamina <= 0:
            return f"Player {first_player.name} does not have enough stamina."
        elif second_player.stamina <= 0:
            return f"Player {second_player.name} does not have enough stamina."

        if first_player.stamina > second_player.stamina:
            first_player, second_player = second_player, first_player
        cls.__attack(first_player, second_player)
        if second_player.stamina <= 0:
            second_player.stamina = 0
            return f"Winner: {first_player.name}"
        first_player, second_player = second_player, first_player
        cls.__attack(first_player, second_player)
        if second_player.stamina <= 0:
            second_player.stamina = 0
            return f"Winner: {first_player.name}"
        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player.name}"
        else:
            return f"Winner: {second_player.name}"

    @staticmethod
    def __attack(first_player: Player, second_player: Player):
        attack = first_player.stamina / 2
        second_player.stamina -= attack

    @staticmethod
    def __check_stamina(first_player: Player, second_player: Player):
        if first_player.stamina <= 0 and second_player.stamina <= 0:
            return f"Player {first_player.name} does not have enough stamina.\n" \
                   f"Player {second_player.name} does not have enough stamina."
        elif first_player.stamina <= 0:
            return f"Player {first_player.name} does not have enough stamina."
        elif second_player.stamina <= 0:
            return f"Player {second_player.name} does not have enough stamina."

    @classmethod
    def __find_players(cls, first_player_name: str, second_player_name: str):
        first_player = None
        second_player = None
        for player in cls.players:
            if player.name == first_player_name:
                first_player = player
        for player in cls.players:
            if player.name == second_player_name:
                second_player = player
        return first_player, second_player

    @classmethod
    def next_day(cls):
        for player in cls.players:
            player.stamina -= player.age * 2
            if player.stamina < 0:
                player.stamina = 0
            cls.sustain(player.name, 'Food')
            cls.sustain(player.name, 'Drink')
