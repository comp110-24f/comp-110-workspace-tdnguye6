"""File to define Bear class."""

__author__: str = "730766559"


class Bear:
    """Bear class with age and hunger_score attributes."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize new Bear objects with age and hunger_score attributes."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Simulate the aging of bears."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Simulate the consumption of fish."""
        self.hunger_score += num_fish
