from DesignPatterns.Builder.CarBuilder.abstract_builder import IBuilder
from DesignPatterns.Builder.CarBuilder.SubObjects.body import Body
from DesignPatterns.Builder.CarBuilder.SubObjects.wheel import Wheel
from DesignPatterns.Builder.CarBuilder.SubObjects.engine import Engine


class Jeep(IBuilder):
    """
    The class which will provide the specifications of the Jeep
    """

    def __init__(self) -> None:
        pass

    def body(self) -> Body:
        """
        A helper function that will return the body of jeep.

        :return: The body of Jeep.
        :rtype: Body
        """

        return Body(color='Green')

    def wheel(self) -> Wheel:
        """
        A helper function that will return the wheel of jeep.

        :return: The wheel for the Jeep
        :rtype: Wheel
        """

        return Wheel(size=20)

    def engine(self) -> Engine:
        """
        A helper function that will return the engine of the jeep.

        :return: The jeep engine
        :rtype: Engine
        """

        return Engine(horsepower=1300)
