from DesignPatterns.Builder.ComputerBuilder.abstract_builder import IBuilder
from DesignPatterns.Builder.ComputerBuilder.computer import Computer


class ComputerDirector:
    """
    A class which will be responsible for creating the Computer.
    """
    def __init__(self, builder: IBuilder) -> None:
        self.__builder = builder

    def get_system(self):
        """
        The function will be used to build the computer.

        :return: The build computer
        :rtype: Computer
        """

        computer = Computer()
        computer.processor(self.__builder.processor())
        computer.hard_disk(self.__builder.hard_disk())
        computer.ram(self.__builder.ram())
        computer.mouse(self.__builder.mouse())
        computer.monitor(self.__builder.monitor())
        computer.keyboard(self.__builder.keyboard())

        return computer
