"""CQ00 Functions"""

__author__ = "730766559"


def mimic(message: str) -> str:
    """Repeat the user's string input back to user"""
    return message


def main() -> None:
    """Print the message 'Howdy!'"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
