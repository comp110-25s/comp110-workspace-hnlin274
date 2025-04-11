"""Tea Party Planning!"""

__author__: str = "730667731"


def main_planner(guests: int) -> None:
    """Cozy Tea Party Planning"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """# of Tea Bags Needed"""
    return people * 2


def treats(people: int) -> int:
    """Amount of Treats"""
    return int((tea_bags(people=people)) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculating Costs of Tea & Treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
