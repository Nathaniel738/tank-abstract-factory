from model.german_tank import GermanTank


class GermanMiddleTank(GermanTank):
    health = 250
    damage = 80
    time_of_shoot = 0.5
    time_of_turn = 1

    def __init__(self) -> None:
        super().__init__()
        print('GermanMiddleTank')
