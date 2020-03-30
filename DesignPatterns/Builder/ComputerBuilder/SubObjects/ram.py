class RAM:
    """
    The RAM that will be used in the CPU of a Computer.
    """

    def __init__(self, capacity: str) -> None:
        self.__capacity = capacity

    def capacity(self) -> str:
        """
        A helper function that will return the capacity of the RAM.

        :return: RAM's capacity
        :rtype: str
        """

        return self.__capacity

    def __str__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        ram = dict()
        ram['Capacity'] = self.__capacity

        return str(ram)

    def __repr__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        return self.__str__()