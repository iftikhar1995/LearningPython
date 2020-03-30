from abc import ABC
from abc import abstractmethod

from DesignPatterns.Builder.ComputerBuilder.SubObjects.hard_disk import HardDisk
from DesignPatterns.Builder.ComputerBuilder.SubObjects.keyboard import KeyBoard
from DesignPatterns.Builder.ComputerBuilder.SubObjects.monitor import Monitor
from DesignPatterns.Builder.ComputerBuilder.SubObjects.mouse import Mouse
from DesignPatterns.Builder.ComputerBuilder.SubObjects.processor import Processor
from DesignPatterns.Builder.ComputerBuilder.SubObjects.ram import RAM


class IBuilder(ABC):
    """
    An interface for the objects that will be build using the computer builder.
    """

    @abstractmethod
    def monitor(self) -> Monitor:
        pass

    @abstractmethod
    def keyboard(self) -> KeyBoard:
        pass

    @abstractmethod
    def mouse(self) -> Mouse:
        pass

    @abstractmethod
    def ram(self) -> RAM:
        pass

    @abstractmethod
    def hard_disk(self) -> HardDisk:
        pass

    @abstractmethod
    def processor(self) -> Processor:
        pass
