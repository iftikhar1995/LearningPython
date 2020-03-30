from DesignPatterns.Builder.CarBuilder.abstract_builder import IBuilder
from DesignPatterns.Builder.CarBuilder.car import Car


class CarDirector:
    """
    A class which will be responsible for creating the car.
    """

    def __init__(self, builder: IBuilder) -> None:
        self. __builder = builder

    def get_car(self) -> Car:
        """
        The function will be used to build the car.
        :return: The object of car
        :rtype: Car
        """

        car = Car()

        car.assemble_engine(self.__builder.engine())

        car.set_body(self.__builder.wheel())

        for i in range(4):
            car.attach_wheel(self.__builder.wheel())

        return car
