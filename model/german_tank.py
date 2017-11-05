from model.tank import Tank


class GermanTank(Tank):
    def __init__(self) -> None:
        super().__init__()
        print('GermanTank')
