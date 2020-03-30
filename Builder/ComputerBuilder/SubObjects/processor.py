class Processor:
    """
    The Processor that will be used in the CPU of a Computer
    """

    def __init__(self, kind: str) -> None:
        self.__kind = kind

    def kind(self) -> str:
        """
        A helper function that will return the type of processor that will be used in the CPU of a computer.

        :return: The type of processor.
        :rtype: str
        """

        return self.__kind

    def __str__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        processor = dict()
        processor['Kind'] = self.__kind
        return str(processor)

    def __repr__(self) -> str:
        """
        Overriding the magic method to send custom representation

        :return: The custom representation of the object
        :rtype: str
        """

        return self.__str__()
