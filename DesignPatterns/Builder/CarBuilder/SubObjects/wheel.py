class Wheel:
    """
    The Wheel of car.
    """

    def __init__(self, size: int) -> None:
        self.__size = size

    def size(self) -> int:
        """
        A helper function that will be used to get the size of the wheel.
        :return:
        """
        return self.__size

    def __repr__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        return self.__str__()

    def __str__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        wheel = dict()
        wheel['Size'] = self.__size

        return str(wheel)
