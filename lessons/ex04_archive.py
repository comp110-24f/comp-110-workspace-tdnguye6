def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Given two lists of integers, iterate over the shortest list and determine
    deep equality between the elements at the same index
    """
    # Initialize a boolean variable that will be updated
    # based on the deep equality of input1 and input2;
    # return when finalized
    equality_update: bool = True

    def check_equality() -> None:
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
