from model.russian_tank import RussianTank


class RussianMiddleTank(RussianTank):
    health = 280
    damage = 100
    time_of_shoot = 0.4
    time_of_turn = 0.8

    def __init__(self) -> None:
        super().__init__()
        print('RussianMiddleTank')
