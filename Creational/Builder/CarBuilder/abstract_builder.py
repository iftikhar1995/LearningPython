from abc import ABC
from abc import abstractmethod

from Creational.Builder.CarBuilder.SubObjects.body import Body
from Creational.Builder.CarBuilder.SubObjects.engine import Engine
from Creational.Builder.CarBuilder.SubObjects.wheel import Wheel


class IBuilder(ABC):
    """
    An interface for the objects that will be build using the Car builder.
    """

    @abstractmethod
    def body(self) -> Body:
        pass

    @abstractmethod
    def wheel(self) -> Wheel:
        pass

    @abstractmethod
    def engine(self) -> Engine:
        pass
