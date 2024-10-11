"""Mutating functions"""

__author__: str = "730766559"


def manual_append(a: list[int], num1: int) -> None:
    a.append(num1)


def double(a: list[int]) -> None:
    idx1: int = 0
    while idx1 < len(a):
        a[idx1] = a[idx1] * 2
        idx1 += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
