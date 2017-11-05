from factory.tank_german_factory import TankGermanFactory
from factory.tank_russian_factory import TankRussianFactory


class App:
    def __init__(self) -> None:
        super().__init__()
        print('Choose tank to create:\n')
        print('1. Russian Tank\n')
        print('2. German Tank\n')
        tank_number = input('To create tank write it number: \n')
        options = {
            1: TankRussianFactory(),
            2: TankGermanFactory()
        }
        if tank_number.isdigit() and int(tank_number) in options:
            tank = options[int(tank_number)]
            tank.create_heavy_tank()
        else:
            print('you typed incorrect data:(')


app = App()
