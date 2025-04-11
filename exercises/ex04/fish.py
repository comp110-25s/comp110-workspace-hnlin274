"""File to define Fish class."""

__author__ = "730667731"


class Fish:
    """Class to represent Fish"""

    age: int

    def __init__(self):
        """Defining __init__ in Fish class."""
        self.age: int = 0
        return None

    def one_day(self):
        """Defining one_day in Fish class"""
        self.age += 1
        return None
