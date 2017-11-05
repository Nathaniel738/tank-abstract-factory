from factory.tank_factory import TankFactory
from factory.tank_german_factory import TankGermanFactory


class App:
    def __init__(self) -> None:
        super().__init__()
        tank_factory = TankGermanFactory()
        tank_factory.create_heavy_tank()



app = App()
# tank_factory = TankFactory()

