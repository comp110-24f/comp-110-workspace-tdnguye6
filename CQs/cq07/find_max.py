"""CQ07 Find maximum number and remove all instances of it in given list"""

__author__: str = "730766559"


def find_and_remove_max(a: list[int]) -> int:
    if len(a) == 0:
        return -1

    max: int = a[0]
    for elem in a:
        if max < elem:
            max = elem

    idx: int = 0
    while idx < len(a):
        if a[idx] == max:
            a.pop(idx)
        else:
            idx += 1

    return max
