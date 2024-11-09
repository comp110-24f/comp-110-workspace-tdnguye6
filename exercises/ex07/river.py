"""File to define River class."""

from ex07.fish import Fish
from ex07.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
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
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(num_fish=3)
                self.remove_fish(amount=3)

    def check_hunger(self):
        updated_bears: list[Bear] = []

        for bear in self.bears:
            if not bear.hunger_score < 0:
                updated_bears.append(bear)

        self.bears = updated_bears

    def repopulate_fish(self):
        return None

    def repopulate_bears(self):
        return None

    def view_river(self) -> None:
        print(f"~~~ Day {str(self.day)}: ~~~ ")
        print(f"Fish population: {str(len(self.fish))} ")
        print(f"Bear population: {str(len(self.bears))} ")

    def one_river_day(self):
        """Simulate one day of life in the river"""
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
        idx: int = 0
        while idx < 7:
            self.one_river_day()
            idx += 1

    def remove_fish(self, amount: int) -> None:
        for idx in range(0, amount):
            self.fish.pop(0)
