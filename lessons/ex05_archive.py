def add_at_index(input: list[int], new_int: int, index: int) -> None:
    """Given a list called input, a given int value called new_int, and a
    given index int value called index, place the given int value at the given
    index of the input list and shift all succeeding elements to the right.
    """
    # Raise an index error if given index is out of range.
    if index < 0 or index >= len(input):
        raise IndexError("Index is out of bounds for the input list")
    # Handle index objection by adding filler element to input list to shift all
    # elements after given index one index to the right.
    input.append(0)
    # Initialize an index called elem for the following while loop to iterate from,
    # where the last element starts excluding the filler element.
    elem: int = len(input) - 2
    # Iterate over all elements starting from last element of input (excluding the
    # filler element) and ending at the given index to assign their values to the
    # index right after their original one.
    while elem >= index:
        input[elem + 1] = input[elem]
        elem -= 1
    # Add the given new_int to the given index.
    input[index] = new_int
