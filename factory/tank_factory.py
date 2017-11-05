from model.tank import Tank


class TankFactory:
    def create_light_tank(self):
        return Tank()

    def create_middle_tank(self):
        return Tank()

    def create_heavy_tank(self):
        return Tank()
