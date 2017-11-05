from model.tank import Tank


class RussianTank(Tank):
    def __init__(self) -> None:
        super().__init__()
        print('RussianTank')
