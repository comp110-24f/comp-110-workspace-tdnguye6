from fish import Fish
from bear import Bear

"""File to define River class."""

__author__: str = "730766559"


class River:
    """River class to simulate a river ecosystem with the days passed in the
    ecosystem, the collection of fish, and the collection of bears in the
    ecosystem.
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
        """Check the age of the entire fish and bear population via fish and bear
        attributes of River class and update the population by simulation
        deaths of fish over the age of 3 and bears over the age of 5.
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
        """When called, simulate the food chain by having every Bear object in
        River 'eat' 3 fish while the fish population is greater than or equal to
        5. Do this by calling eat() method from Bear class and remove_fish()
        method from River class.
        """
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(num_fish=3)
                self.remove_fish(amount=3)

    def check_hunger(self):
        """When called, simulate the 'death' of all bears whose hunger_score
        is less than 0 and update the River object's bear population in accordance.
        """
        updated_bears: list[Bear] = []

        for bear in self.bears:
            if not bear.hunger_score < 0:
                updated_bears.append(bear)

        self.bears = updated_bears

    def repopulate_fish(self):
        """When called, simulate the reproduction of fish by increasing
        the population of fish by 4 for every 2 fish in the concurrent
        population.
        """
        fish_count: int = len(self.fish)
        offspring_count: int = (fish_count // 2) * 4
        for offspring in range(0, offspring_count):
            self.fish.append(Fish())

    def repopulate_bears(self):
        """When called, simulate the reproduction of fish by increasing
        the population of bears by 1 for every 2 bears in the concurrent
        population.
        """
        bear_count: int = len(self.bears)
        offspring_count: int = bear_count // 2

        for offspring in range(0, offspring_count):
            self.bears.append(Bear())

    def view_river(self) -> None:
        """When called, print the attributes of the River object upon which
        this method is called.
        """
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
        """Call one_river_day() method 7 times to simulate a week of the
        river simulation.
        """
        idx: int = 0
        while idx < 7:
            self.one_river_day()
            idx += 1

    def remove_fish(self, amount: int) -> None:
        """When called, after having passed the argument for the number
        of fish to be removed from self.fish, remove that same number of fish
        from the population, starting from the frontmost indices of the
        self.fish list.
        """
        for idx in range(0, amount):
            self.fish.pop(0)
