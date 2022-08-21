import sys
from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    __valid_types_horse_breeds = ["Appaloosa", "Thoroughbred"]

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type in self.__valid_types_horse_breeds:
            for horse in self.horses:
                if horse_name == horse.name:
                    raise Exception(f"Horse {horse_name} has been already added!")

            if horse_type == "Appaloosa":
                self.horses.append(Appaloosa(horse_name, horse_speed))
            elif horse_type == "Thoroughbred":
                self.horses.append(Thoroughbred(horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for jokey in self.jockeys:
            if jockey_name == jokey.name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race_type == race.race_type:
                raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                for i in range(len(self.horses) -1, -1, -1):
                    horse = self.horses[i]
                    if horse.__class__.__name__ == horse_type and not horse.is_taken:
                        if jockey.horse:
                            raise Exception(f"Jockey {jockey_name} already has a horse.")
                        jockey.horse = horse
                        horse.is_taken = True
                        return f"Jockey {jockey_name} will ride the horse {horse.name}."
                raise Exception(f"Horse breed {horse_type} could not be found!")

        else:
            raise Exception(f"Jockey {jockey_name} could not be found!")

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                for jokey in self.jockeys:
                    if jokey.name == jockey_name:
                        if not jokey.horse:
                            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
                        for horse_race in self.horse_races:
                            if jokey in horse_race.jockeys:
                                raise Exception(f"Jockey {jockey_name} has been already added to the {race_type} race.")

                        race.jockeys.append(jokey)
                        return f"Jockey {jockey_name} added to the {race_type} race."

                else:
                    raise Exception(f"Jockey {jockey_name} could not be found!")

        else:
            raise Exception(f"Race {race_type} could not be found!")

    def start_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                if len(race.jockeys) < 2:
                    raise Exception(f"Horse race {race_type} needs at least two participants!")

                highest_speed = -sys.maxsize
                j_name = None
                h_name = None
                for jockey in race.jockeys:
                    if jockey.horse.speed > highest_speed:
                        highest_speed = jockey.horse.speed
                        j_name = jockey.name
                        h_name = jockey.horse.name
                return f"The winner of the {race_type} race, " \
                       f"with a speed of {highest_speed}km/h is {j_name}! Winner's horse: {h_name}."

        else:
            raise Exception(f"Race {race_type} could not be found!")
