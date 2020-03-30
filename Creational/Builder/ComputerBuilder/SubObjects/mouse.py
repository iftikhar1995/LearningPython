class Mouse:
    """
    The mouse of a computer.
    """

    def __init__(self, kind: str) -> None:
        self.__kind = kind

    def kind(self) -> str:
        """
        A helper function that will return the type of the mouse associated with the computer.

        :return: The type of mouse.
        :rtype: str
        """

        return self.__kind

    def __str__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        mouse = dict()
        mouse['Kind'] = self.__kind

        return str(mouse)

    def __repr__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        return self.__str__()

