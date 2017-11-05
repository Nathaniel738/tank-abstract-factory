from model.german_tank import GermanTank


class GermanHeavyTank(GermanTank):
    health = 500
    damage = 150
    time_of_shoot = 1
    time_of_turn = 2

    def __init__(self) -> None:
        super().__init__()
        print('GermanHeavyTank')
