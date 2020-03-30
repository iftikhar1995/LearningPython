class HardDisk:
    """
    HardDisk of a computer
    """

    def __init__(self, capacity: str) -> None:
        self.__capacity = capacity

    def capacity(self) -> str:
        """
        A helper function that will return the capacity of the hard disk.

        :return: The capacity of the hard disk.
        :rtype: str
        """

        return self.__capacity

    def __str__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        disk = dict()
        disk['Capacity'] = self.__capacity

        return str(disk)

    def __repr__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        return self.__str__()
