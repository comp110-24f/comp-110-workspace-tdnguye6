"""More list utility functions for EX05"""

__author__: str = "730766559"


def only_evens(input: list[int]):
    """For every even number in given list of ints named input, return a different list
    populated with those even numbers.
    """
    # Initialize an empty list of ints.
    new_list: list[int] = []
    # Iterate over entire input list and append new_list with every even number.
    for elem in input:
        if elem % 2 == 0:
            new_list.append(elem)
    return new_list


def sub(input: list[int], start: int, end: int):
    """Given two ints representing the start and end index, return a
    list populated with the elements between the given indices, including
    the start index and excluding the end index.
    """
    new_list: list[int] = []

    # Return an unpopulated new_list if the given start and end indices are edge cases
    if start >= len(input) or len(input) == 0 or end <= 0:
        return new_list
    # Let the first element of the new_list be the 0th index of input if given start int
    # is negative.
    if start < 0:
        start = 0
    # Let the last element of the new_list be the "len(input)"th index (last index) of
    # input if given end int is higher than the length of the input.
    if end > len(input):
        end = len(input)

    # Initialize an index for a while loop that iterates over the range of input list
    # defined by the given start and end indices. Append the elements of input over
    # this range to new_list.
    idx: int = start
    while idx < (end):
        new_list.append(input[idx])
        idx += 1

    return new_list


def add_at_index(input: list[int], new_int: int, index: int) -> None:
    """Given a list of ints called input, assign new_int to the "index"th element
    of the list after shifting all elements from and including the "index"th element
    to the right by one index.
    """
    # Throw an index error if the given index is out of the range of the given list.
    if index < 0 or index > len(input):
        raise IndexError("Index is out of bounds for the input list")

    # Make room in the list for the elements to the right of the "index"th element of
    # input to be shifted once.
    input.append(0)
    # Access a range of integers between the index of the last element of input and the
    # given index with a step of -1 to simulate going backwards in the list.
    # For the elements after the "index"th element, assign the element +1 index
    # away to itself.
    for i in range(len(input) - 1, index, -1):
        input[i] = input[i - 1]
    # Assign new_int to the given index
    input[index] = new_int
