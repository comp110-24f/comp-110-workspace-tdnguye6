"""File to define Fish class."""

__author__: str = "730766559"


class Fish:
    """Fish class to simulate a fish in a river ecosystem with an age."""

    age: int

    def __init__(self):
        """Initialize the age of new Fish objects to the int value of 0."""

        self.age = 0

    def one_day(self) -> None:
        """Simulate the aging of fish by adding 1 to the age attribute."""

        self.age += 1
