class KeyBoard:
    """
    The keyboard of a computer.
    """

    def __init__(self, layout: str) -> None:
        self.__layout = layout

    def layout(self) -> str:
        """
        A helper function to return the layout of the keyboard.

        :return: The keyboard's layout.
        :rtype: str
        """

        return self.__layout

    def __str__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        keyboard = dict()
        keyboard['Layout'] = self.__layout

        return str(keyboard)

    def __repr__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        return self.__str__()
