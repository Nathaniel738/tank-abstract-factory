from model.russian_tank import RussianTank


class RussianLightTank(RussianTank):
    health = 110
    damage = 25
    time_of_shoot = 0.2
    time_of_turn = 0.4

    def __init__(self) -> None:
        super().__init__()
        print('RussianLightTank')
