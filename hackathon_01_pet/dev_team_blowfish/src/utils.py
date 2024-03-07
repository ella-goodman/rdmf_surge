class SingletonIDGenerator:
    """A class that generates unique IDs using a singleton pattern.

    Attributes
    ----------
    start : int
        The starting value of the ID sequence.
    step : int
        The increment value of the ID sequence.

    Examples
    --------
    >>> id_gen = SingletonIDGenerator(start=100, step=10)
    >>> next(id_gen)
    100
    >>> next(id_gen)
    110
    >>> id_gen2 = SingletonIDGenerator(start=200, step=20)
    >>> next(id_gen2)
    120
    """

    _instance = None

    def __new__(cls, start: int = 0, step: int = 1):
        """Create a new instance of the class or return the existing one.

        Parameters
        ----------
        start : int, optional
            The starting value of the ID sequence, by default 0
        step : int, optional
            The increment value of the ID sequence, by default 1

        Returns
        -------
        SingletonIDGenerator
            The singleton instance of the class.
        """
        if cls._instance is None:
            cls._instance = super(SingletonIDGenerator, cls).__new__(cls)
            cls._instance.start = start
            cls._instance.step = step
        return cls._instance

    def __init__(self, start: int = 0, step: int = 1) -> None:
        """Initialize the instance attributes.

        Parameters
        ----------
        start : int, optional
            The starting value of the ID sequence, by default 0
        step : int, optional
            The increment value of the ID sequence, by default 1
        """
        self.start: int = start
        self.step: int = step

    def __iter__(self):
        """Return the iterator object of the instance.

        Returns
        -------
        SingletonIDGenerator
            The iterator object of the instance.
        """
        return self

    def __next__(self) -> int:
        """Return the next ID in the sequence.

        Returns
        -------
        int
            The next ID in the sequence.
        """
        value: int = self.start
        self.start += self.step
        return value

    def reset(self, reset_val: int = 0) -> None:
        self.start = reset_val
