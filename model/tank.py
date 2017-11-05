class Tank:
    health = 0
    damage = 0
    time_of_shoot = 0
    time_of_turn = 0

    def __init__(self) -> None:
        super().__init__()
        print('Tank')
