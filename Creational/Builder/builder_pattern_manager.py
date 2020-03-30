from Creational.Builder.CarBuilder.car_director import CarDirector
from Creational.Builder.CarBuilder.jeep import Jeep
from Creational.Builder.ComputerBuilder.computer_director import ComputerDirector
from Creational.Builder.ComputerBuilder.hp_probook import HPProBook


class BuilderPatternManager:

    def __init__(self):
        pass

    @staticmethod
    def build_jeep():
        jeep = Jeep()
        director = CarDirector(builder=jeep)
        return director.get_car()

    @staticmethod
    def build_hp_probook():
        probook = HPProBook()
        director = ComputerDirector(probook)
        return director.get_system()


def main():
    # Creating a Jeep
    jeep = BuilderPatternManager.build_jeep()
    print(type(jeep))
    print(jeep)

    # Creating a P4 Computer
    hp_probook = BuilderPatternManager.build_hp_probook()
    print(type(hp_probook))
    print(hp_probook)


if __name__ == '__main__':
    main()
