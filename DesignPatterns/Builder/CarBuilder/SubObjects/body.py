class Body:
    """
    The body of a car.
    """

    def __init__(self, color: str) -> None:
        self.__color = color

    def color(self) -> str:
        """
        A helper function that will return the color of the body

        :return: The body color
        :rtype: str
        """

        return self.__color

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

        body = dict()
        body['Color'] = self.__color

        return str(body)
