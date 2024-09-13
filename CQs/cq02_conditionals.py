"""Practice with conditionals, Local Variables, and User Input"""

__author__: str = "730766559"


def guess_a_number() -> None:
    """Take user input for a number and compare equivalence to secret int variable"""
    secret: int = 7
    x = input("Guess a number: ")
    print("Your guess was " + str(x))
    if int(x) == secret:
        print("You got it!")
    if int(x) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    if int(x) > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
