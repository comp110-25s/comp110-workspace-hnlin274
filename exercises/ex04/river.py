"""File to define River class."""

__author__ = "730667731"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """Class to represent River."""

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Defining check_ages for River class."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]
        return None

    def bears_eating(self):
        """Defining bears_eating for River class."""
        for item in range(len(self.bears)):
            if len(self.fish) >= 5:
                self.remove_fish(3)
        for item in self.bears:
            item.eat(3)
        return None

    def check_hunger(self):
        """Defining check_hunger for River class."""
        bears: list[Bear] = []
        for item in self.bears:
            if item.hunger_score >= 0:
                bears.append(item)
        self.bears = bears
        return None

    def repopulate_fish(self):
        """Defining repopulate_fish for River class."""
        new_fish: int = (len(self.fish) // 2) * 4
        for i in range(new_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Defining repopulate_bears for River class."""
        new_bears: int = len(self.bears) // 2
        for i in range(new_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Defining view_river for River class."""
        x = self.day
        y = len(self.fish)
        z = len(self.bears)
        print(f"~~~ Day {x}: ~~~")
        print(f"Fish population: {y}")
        print(f"Bear population: {z}")
        return None

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

    def one_river_week(self):
        """Defining one_river_week in River class."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int):
        """Defining remove_fish in River class."""
        for i in range(amount):
            self.fish.pop(i)
