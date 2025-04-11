"""File to define Bear class."""

__author__ = "730667731"


class Bear:
    """Class to represent bear"""

    age: int
    hunger_score: int

    def __init__(self):
        """Defining __init__ in Bear class."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        """Defining eat in Bear class."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Defining eat in Bear class."""
        self.hunger_score += num_fish
