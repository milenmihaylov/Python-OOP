from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    _MAX_SPEED = 120
    _TRAIN_SPEED_INCREASE = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

