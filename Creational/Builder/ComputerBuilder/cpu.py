from Creational.Builder.ComputerBuilder.SubObjects.hard_disk import HardDisk
from Creational.Builder.ComputerBuilder.SubObjects.processor import Processor
from Creational.Builder.ComputerBuilder.SubObjects.ram import RAM


class CPU:
    """
    A class which will be responsible for creating the CPU for a Computer.
    """

    def __init__(self) -> None:
        self.__ram = None
        self.__hard_disk = None
        self.__processor = None

    def ram(self, ram: RAM) -> None:
        """
        A helper function that will add the RAM to CPU.

        :param ram: The RAM of the CPU.
        :type ram: RAM
        :return:
        """

        self.__ram = ram

    def hard_disk(self, hard_disk: HardDisk) -> None:
        """
        A helper function that will add the hard disk to CPU.

        :param hard_disk: The hard disk of the CPU.
        :type hard_disk: HardDisk
        :return:
        """

        self.__hard_disk = hard_disk

    def processor(self, processor: Processor) -> None:
        """
        A helper function that will add the Processor to CPU.

        :param processor: The processor of the CPU
        :type processor: Processor
        :return:
        """

        self.__processor = processor

    def __str__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        cpu = dict()
        cpu['RAM'] = self.__ram
        cpu['HardDisk'] = self.__hard_disk
        cpu['Processor'] = self.__processor

        return str(cpu)

    def __repr__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        return self.__str__()
