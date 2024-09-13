"""Plan a cozy tea party by asking user for number of guests and calculating number of tea bags needed."""

__author__: str = "730656115"  # My PID


def main_planner(guests: int) -> None:
    """Write an outline for number of guests, tea bags, treats, and their costs"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """Calculate the number of teabags"""
    return people * 2  # on average 2 teabags a person


def treats(people: int) -> int:
    """Calculate number of treats based on number of guests"""
    return int(tea_bags(people=people) * 1.5)  # On average, 1.5 treats per teabags


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate total cost"""
    return (tea_count * 0.50) + (
        treat_count * 0.75
    )  # a tea cost $0.50 and a treat costs $0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
