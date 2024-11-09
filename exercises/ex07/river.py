"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


__author__: str = "730766559"


class River:
    """River class to simulate a river ecosystem.

    The days passed in the river ecosystem, the collection
    of fish, and the collection of bears in the river
    ecosystem are given int, list[Fish], and list[Bear]
    attributes.
    """

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Update the entire fish and bear population by checking their ages.

        Simulate the deaths of the fish and bear population by checking the
        age attributes of the fish and bears.
        """
        updated_fish: list[Fish] = []
        updated_bears: list[Bear] = []

        for elem1 in range(0, len(self.fish)):
            if self.fish[elem1].age <= 3:
                updated_fish.append(self.fish[elem1])

        for elem2 in range(0, len(self.bears)):
            if self.bears[elem2].age <= 5:
                updated_bears.append(self.bears[elem2])

        self.fish = updated_fish
        self.bears = updated_bears

    def bears_eating(self):
        """Simulate the food chain between the bears and fish.

        Every bear will 'eat' 3 fish while the fish population
        is greater than or equal to 5. Do this by calling eat()
        method from Bear class and remove_fish() method
        from River class.
        """
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(num_fish=3)
                self.remove_fish(amount=3)

    def check_hunger(self):
        """When called, simulate the starvation of bears.

        Check the hunger_score attribute of every bear and if it
        is less than 0, update the River object's bear population
        accordingly.
        """
        updated_bears: list[Bear] = []

        for bear in self.bears:
            if not bear.hunger_score < 0:
                updated_bears.append(bear)

        self.bears = updated_bears

    def repopulate_fish(self):
        """Simulate the reproduction of fish.

        Increase the population of fish by 4 for every 2 fish in the concurrent
        population.
        """
        fish_count: int = len(self.fish)
        offspring_count: int = (fish_count // 2) * 4
        for offspring in range(0, offspring_count):
            self.fish.append(Fish())

    def repopulate_bears(self):
        """Simulate the reproduction of fish.

        Increase the population of bears by 1 for every 2 bears in the concurrent
        population.
        """
        bear_count: int = len(self.bears)
        offspring_count: int = bear_count // 2

        for offspring in range(0, offspring_count):
            self.bears.append(Bear())

    def view_river(self) -> None:
        """Print the attributes of the River object upon which this method is called."""
        print(f"~~~ Day {str(self.day)}: ~~~ ")
        print(f"Fish population: {str(len(self.fish))} ")
        print(f"Bear population: {str(len(self.bears))} ")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Call one_river_day() method 7 times to simulate a week."""
        idx: int = 0
        while idx < 7:
            self.one_river_day()
            idx += 1

    def remove_fish(self, amount: int) -> None:
        """When called, remove a given number of fish from the population.

        Start from the frontmost indices of the self.fish list.
        """
        for idx in range(0, amount):
            self.fish.pop(0)
