from Creational.Builder.CarBuilder.SubObjects.body import Body
from Creational.Builder.CarBuilder.SubObjects.engine import Engine
from Creational.Builder.CarBuilder.SubObjects.wheel import Wheel


class Car:
    """
    A class that will be the product of the builder
    """

    def __init__(self) -> None:
        self.__engine = None
        self.__body = None
        self.__wheels = list()

    def set_body(self, body: Body) -> None:
        """
        A helper function that will set the body of the car.

        :param body: The body to attach with car.
        :type body: Body
        :return:
        """

        self.__body = body

    def attach_wheel(self, wheel: Wheel) -> None:
        """
        A helper function that will attach the wheels to the car.

        :param wheel: The wheel to attach with car.
        :type wheel: Wheel
        :return:
        """

        self.__wheels.append(wheel)

    def assemble_engine(self, engine: Engine) -> None:
        """
        A helper function that will attach the engine to the car.

        :param engine: The engine to attach
        :type engine: Engine
        :return:
        """

        self.__engine = engine

    def __str__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        car = dict()
        car['Engine'] = self.__engine
        car['Wheels'] = self.__wheels
        car['Body'] = self.__body

        return str(car)

    def __repr__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        return self.__str__()
