from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.valid_name} has already joined"
        self.__players.append(player)
        return f"Player {player.valid_name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for i, player in enumerate(self.__players):
            if player.valid_name == player_name:
                self.__players.pop(i)
                return player
        return f"Player {player_name} not found"
    