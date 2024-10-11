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
    if len(input) == 0:
        return False
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
    """Compare every element at every index of given list input1 to given list input2"""
    # Return true if both lists are empty
    if input1 == [] and input2 == []:
        return True
    # Return false if either list is empty
    if input1 == [] or input2 == []:
        return False
    # Return false if the lists are of different lengths
    if len(input1) > len(input2) or len(input1) < len(input2):
        return False
    # Initialize a variable to be updated to indicate deep equality of both lists
    equality_update: bool
    # Initialize an index variable as the condition of loop iterating over indices of
    # the lists
    index: int = 0
    # Loop over every index of input1 and compare to elements of the same indices in
    # input2, updating equality_update until all iterations of the loop complete
    if len(input1) == len(input2):
        while index < len(input1):
            if input1[index] == input2[index]:
                equality_update = True
            else:
                equality_update = False
            index += 1

    return equality_update


def extend(input1: list[int], input2: list[int]) -> None:
    """Append every element from input2 to input1"""

    index: int = 0
    # Iterate over and append every element in input2 to input1 from the starting element
    # to the last element
    while index < len(input2):
        input1.append(input2[index])
        index += 1
