from Creational.Builder.ComputerBuilder.SubObjects.hard_disk import HardDisk
from Creational.Builder.ComputerBuilder.SubObjects.keyboard import KeyBoard
from Creational.Builder.ComputerBuilder.SubObjects.monitor import Monitor
from Creational.Builder.ComputerBuilder.SubObjects.mouse import Mouse
from Creational.Builder.ComputerBuilder.SubObjects.processor import Processor
from Creational.Builder.ComputerBuilder.SubObjects.ram import RAM
from Creational.Builder.ComputerBuilder.abstract_builder import IBuilder


class HPProBook(IBuilder):
    """
    The class which will provide the specifications of the HP ProBook
    """

    def __init__(self) -> None:
        pass

    def monitor(self) -> Monitor:
        """
        A helper function that will return the monitor of a computer.

        :return: The monitor of probook
        :rtype: Monitor
        """

        return Monitor('1024 x 1024')

    def keyboard(self) -> KeyBoard:
        """
        A helper function that will return the keyboard of a computer.

        :return: The Keyboard of a computer.
        :rtype: KeyBoard
        """

        return KeyBoard('US')

    def mouse(self) -> Mouse:
        """
        A helper function that will return the mouse of a computer.

        :return: The mouse of the computer.
        :rtype: Mouse
        """

        return Mouse('Wireless')

    def ram(self) -> RAM:
        """
        A helper function that will return the ram of a computer.

        :return: The RAM of a computer.
        :rtype: RAM
        """

        return RAM('8 GB')

    def hard_disk(self) -> HardDisk:
        """
        A helper function that will return the Hard Disk of a computer.

        :return: The computer's hard disk
        :rtype: HardDisk
        """

        return HardDisk('500 GB')

    def processor(self) -> Processor:
        """
        A helper function that will return the processor of a computer.

        :return: The computer's processor
        :rtype: Processor
        """

        return Processor('Intel I3 - 3rd Generation')
