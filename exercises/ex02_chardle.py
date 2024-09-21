"""EX02 - Chardle - A cute step towards Wordle."""

__author__ = "730766559"


def input_word() -> str:
    """Prompt user input for a 5-char word and return a string."""
    # Assign a string variable to prompted user input for 5-char word.
    five_char_word: str = input("Enter a 5-character word: ")
    # Check if user input has 5 characters. Print error message if not the case.
    if len(five_char_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    # Print the user's input.
    print(f"'{five_char_word}'")
    return five_char_word


def input_letter() -> str:
    """Prompt user for a single letter to check five_char_word for and return a string."""
    # Assign a string variable to prompted user input for a single letter.
    match_letter: str = input("Enter a single character: ")
    # Check if user input is a single character. Print error message if not the case.
    if len(match_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    # Print the user's input.
    print(f"'{match_letter}'")
    return match_letter


def contains_char(word: str, letter: str) -> None:
    """Search for user inputted letter in user inputted word."""
    print(f"Searching for {letter} in {word}")
    # Initialize integer variable index to iterate over word.
    index: int = 0
    # Initialize integer variable match_count to tally # of instances of letter in word.
    match_count: int = 0
    # Iterate over all 5 letters of word to see # of matches.
    # If the current working index of word is equivalent to letter, print a confirming
    # message.
    # For every instance of letter found in word, add 1 to match_count.
    if word[index] == letter:
        print(f"{letter} found at index {index}")
        match_count += 1
    index += 1
    if word[index] == letter:
        print(f"{letter} found at index {index}")
        match_count += 1
    index += 1
    if word[index] == letter:
        print(f"{letter} found at index {index}")
        match_count += 1
    index += 1
    if word[index] == letter:
        print(f"{letter} found at index {index}")
        match_count += 1
    index += 1
    if word[index] == letter:
        print(f"{letter} found at index {index}")
        match_count += 1
    # Print the number of instances of letter found in word depending on value of
    # match_count.
    if match_count == 0:
        print(f"No instances of {letter} found in {word}")
    elif match_count == 1:
        print(f"1 instance of {letter} found in {word}")
    else:
        print(f"{match_count} instances of {letter} found in {word}")


def main() -> None:
    """Run the chardle program"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
