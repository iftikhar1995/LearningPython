from Creational.Builder.ComputerBuilder.SubObjects.hard_disk import HardDisk
from Creational.Builder.ComputerBuilder.SubObjects.keyboard import KeyBoard
from Creational.Builder.ComputerBuilder.SubObjects.monitor import Monitor
from Creational.Builder.ComputerBuilder.SubObjects.mouse import Mouse
from Creational.Builder.ComputerBuilder.SubObjects.processor import Processor
from Creational.Builder.ComputerBuilder.SubObjects.ram import RAM
from Creational.Builder.ComputerBuilder.cpu import CPU


class Computer:
    """
    A class that will be the product of the builder
    """

    def __init__(self) -> None:
        self.__monitor = None
        self.__cpu = CPU()
        self.__keyboard = None
        self.__mouse = None

    def monitor(self, monitor: Monitor) -> None:
        """
        A helper function that will add the monitor to the computer.

        :param monitor: The monitor that is going to be associated with the computer.
        :type monitor: Monitor
        :return:
        """

        self.__monitor = monitor

    def keyboard(self, keyboard: KeyBoard) -> None:
        """
        A helper function that will add the keyboard to the computer.

        :param keyboard: The keyboard of the computer
        :type keyboard: KeyBoard
        :return:
        """

        self.__keyboard = keyboard

    def mouse(self, mouse: Mouse) -> None:
        """
        A helper function that will add the mouse to the computer.

        :param mouse: The mouse of a computer.
        :type mouse: Mouse
        :return:
        """

        self.__mouse = mouse

    def ram(self, ram: RAM) -> None:
        """
        A helper function that will add the ram to the computer.

        :param ram: The ram of the computer.
        :type ram: RAM
        :return:
        """

        self.__cpu.ram(ram)

    def hard_disk(self, hard_disk: HardDisk) -> None:
        """
        A helper function that will add the hard disk to the computer.

        :param hard_disk: The hard disk of the computer.
        :type hard_disk: HardDisk
        :return:
        """

        self.__cpu.hard_disk(hard_disk)

    def processor(self, processor: Processor) -> None:
        """
        A helper function that will add the processor to the computer.

        :param processor: The processor of the computer.
        :type processor: Processor
        :return:
        """

        self.__cpu.processor(processor)

    def __str__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        computer = dict()
        computer['Monitor'] = self.__monitor
        computer['Mouse'] = self.__mouse
        computer['KeyBoard'] = self.__keyboard
        computer['CPU'] = self.__cpu

        return str(computer)

    def __repr__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        return self.__str__()
