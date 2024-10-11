"""Ex04 List Utils"""

__author__: str = "730766559"


def all(input: list[int], match_input: int) -> bool:
    """Iterate over list called vals and return True if all elements in vals
    are equal to int variable match_val, else return False
    """
    # Initialize boolean variable match_update as condition for final return value
    match_update: bool
    # Iterate over entire vals list and return False if a non-matching element
    # is encountered. Else, return True if loop completes
    for elem in input:
        if match_input == elem:
            match_update = True
        else:
            return False
    return match_update


def max(input: list[int]) -> int:
    """Iterate over a list of ints called input and return the largest integer"""
    # Raise an error if an empty list is provided as input
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    # Iterating over the entire input list, pop off all integers except the largest
    # until one element remains
    while len(input) > 1:
        if input[0] <= input[1]:
            input.pop(0)
        else:
            input.pop(1)
    return input[0]


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Given two lists of integers, iterate over the shortest list and determine
    deep equality between the elements at the same index
    """
    # Initialize a boolean variable that will be updated
    # based on the deep equality of input1 and input2;
    # return when finalized
    equality_update: bool = True

    def check_equality():
        """Given two lists of equal len, iterate over both lists and determine if
        all elements are equal at the same indices
        """
        for elem1 in input1:
            for elem2 in input2:
                if elem1 == elem2:
                    equality_update = True
                else:
                    equality_update = False

    # Assign an int variable to the difference in length between input1 and input2
    # and use as comparison condition to handle lists of varied length
    len_diff: int = len(input1) - len(input2)
    # If input1 and input2 are of equal length, check for deep equality
    if len_diff == 0:
        check_equality()
    # If input1 is shorter than input2, ignore elements in input2 that are in indices
    # beyond input1's range
    elif len_diff < 0:
        while len(input1) < len(input2):
            input2.pop(len(input2) - 1)
        check_equality()
    # If input1 is longer than input2, ignore elements in input1 that are in indices
    # beyond input2's range
    elif len_diff > 0:
        while len(input2) < len(input1):
            input1.pop(len(input1) - 1)
        check_equality()

    return equality_update


def extend(input1: list[int], input2: list[int]) -> None:
    """Append every element from input2 to input1"""
    # Initialize an int variable as an index condition to append every element
    # from input2 to input1
    index: int = len(input2)
    # Iterate over the entire input2 list, appending each element as indexed to input1
    while 0 < index:
        input1.append(input2[index - 1])
        index -= 1
