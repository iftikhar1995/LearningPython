class Monitor:
    """
    The mouse of the computer.
    """

    def __init__(self, resolution: str) -> None:
        self.__resolution = resolution

    def resolution(self) -> str:
        """
        A helper function the will return the resolution of the monitor.

        :return: The screen resolution.
        :rtype: str
        """

        return self.__resolution

    def __str__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        monitor = dict()
        monitor['Resolution'] = self.__resolution

        return str(monitor)

    def __repr__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        return self.__str__()
