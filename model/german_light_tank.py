from model.german_tank import GermanTank


class GermanLightTank(GermanTank):
    health = 100
    damage = 20
    time_of_shoot = 0.3
    time_of_turn = 0.5

    def __init__(self) -> None:
        super().__init__()
        print('GermanLightTank')
