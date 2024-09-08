"""Ex01: Calculate # of refreshments and cost of tea party given # of guests"""

__author__: str = "730766559"


def main_planner(guests: int) -> None:
    """Program entrypoint"""

    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculate number of tea bags given number of guests"""
    return 2 * people


def treats(people: int) -> int:
    """Calculate number of treats given value of tea_bags"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost of tea party given tea_count and treat_count"""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
