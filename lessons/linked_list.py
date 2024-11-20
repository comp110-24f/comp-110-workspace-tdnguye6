"""Exploring linked lists in lecture"""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next

    def __str__(self) -> str:
        rest: str = ""
        if self.next is None:  # Base case
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def last(head: Node) -> int:
    if head.next is None:  # Base case
        return head.value
    else:  # Recursive case
        return last(head.next)


two: Node = Node(2, None)
one: Node = Node(1, two)
print(one)
print(last(one))
