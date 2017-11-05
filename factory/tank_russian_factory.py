from factory.tank_factory import TankFactory
from model.russian_heavy_tank import RussianHeavyTank
from model.russian_light_tank import RussianLightTank
from model.russian_middle_tank import RussianMiddleTank


class TankRussianFactory(TankFactory):
    def create_light_tank(self):
        return RussianLightTank()

    def create_middle_tank(self):
        return RussianMiddleTank()

    def create_heavy_tank(self):
        return RussianHeavyTank()
