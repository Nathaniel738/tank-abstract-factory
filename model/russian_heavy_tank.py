from model.russian_tank import RussianTank


class RussianHeavyTank(RussianTank):
    health = 500
    damage = 300
    time_of_shoot = 1
    time_of_turn = 1.9

    def __init__(self) -> None:
        super().__init__()
        print('RussianHeavyTank')
