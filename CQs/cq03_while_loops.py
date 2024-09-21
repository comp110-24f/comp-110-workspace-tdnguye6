"""Practicing a while loop iterated over a string"""

__author__: str = "730766559"


def num_instances(phrase: str, search_char: str) -> int:
    """Count number of times a given character appears in a string literal phrase"""
    # Initalize a local variable to count # of times search_char appears in phrase.
    count: int = 0
    # Initialize a local variable to be an index for the condition of the while loop
    # to iterate over until exit. Iterates over last character of phrase to first
    # character.
    index: int = len(phrase) - 1
    # Iterate over phrase string and add to count for every instance search_char appears
    # in phrase string. The local int variable index serves as exit condition
    while index >= 0:
        if phrase[index] == search_char:
            count += 1
        index -= 1
    return count
