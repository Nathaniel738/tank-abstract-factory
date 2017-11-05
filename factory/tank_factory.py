import abc


class TankFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_light_tank(self):
        pass

    @abc.abstractmethod
    def create_middle_tank(self):
        pass

    @abc.abstractmethod
    def create_heavy_tank(self):
        pass
