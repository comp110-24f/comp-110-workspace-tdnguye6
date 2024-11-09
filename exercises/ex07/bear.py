"""File to define Bear class."""

__author__: str = "730766559"


class Bear:
    """Bear class to simulate a bear in a river ecosystem with an age
    and hunger metric.
    """

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize new Bear objects with an age int value of 0 and
        a hunger_score int value of 0.
        """
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Simulate the aging of bears and their caloric decrement
        by adding 1 to age and subtracting 1 from the hunger_score.
        """
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Simulate the consumption of fish by bears by increasing the
        hunger_score by the same number as there were fish.
        """
        self.hunger_score += num_fish
