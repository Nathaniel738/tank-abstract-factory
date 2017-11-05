from factory.tank_factory import TankFactory
from model.german_heavy_tank import GermanHeavyTank
from model.german_light_tank import GermanLightTank
from model.german_middle_tank import GermanMiddleTank


class TankGermanFactory(TankFactory):
    def create_light_tank(self):
        return GermanLightTank()

    def create_middle_tank(self):
        return GermanMiddleTank()

    def create_heavy_tank(self):
        return GermanHeavyTank()
