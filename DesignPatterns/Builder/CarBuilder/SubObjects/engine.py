class Engine:
    """
    The engine of a car
    """

    def __init__(self, horsepower: int) -> None:
        self.__horsepower = horsepower

    def horsepower(self) -> int:
        """
        A helper function that will be used to get the horsepower of the engine.

        :return: Horsepower of the engine
        :rtype: int
        """

        return self.__horsepower

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

        engine = dict()
        engine['HorsePower'] = self.__horsepower

        return str(engine)
