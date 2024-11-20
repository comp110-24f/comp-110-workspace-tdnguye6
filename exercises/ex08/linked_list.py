"""Linked lists utils for EX08."""

from __future__ import annotations


class Node:
    """Class defining a linked list."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Initialize linked list with arguments passed.

        Node value is initialized with an int and next is either a linked node
        or None, where the end the linked list is.
        """
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Magic method that implicitly gives the linked list a str visualizer."""
        rest: str = ""
        if self.next is None:  # Base case
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def last(head: Node) -> int:
    """Given a linked list, return the value of the last node."""
    if head.next is None:  # Base case
        return head.value
    else:  # Recursive case
        return last(head.next)


def value_at(head: Node | None, index: int) -> int:
    """Return the value of the node at the given index given a linked list."""
    # Raise an IndexError if no linked list is given.
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    # Base case, when index = 0, return the value.
    if index == 0:
        return head.value
    # Edge case where an IndexError is raised if the given index does not exist
    elif index < 0:
        raise IndexError("Index is out of bounds on the list.")
    # Recursive case that progresses towards the desired node.
    else:
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Given a linked list, return the max value among the nodes."""
    # Raise a ValueError if the given linked list is None.
    if head is None:
        raise ValueError("Cannot call max with None")

    # Base case if there is only one node.
    if head.next is None:
        return head.value

    # Recursive case that progresses until the base case is reached.
    max_rest = max(head.next)

    # The max value among the rest of the nodes is returned as the recursion
    # regresses back to the previous max() calls in the memory stack.
    if head.value > max_rest:
        return head.value
    else:
        return max_rest


def linkify(items: list[int]) -> Node | None:
    """Given a list of elements, turn them into nodes of a linked list."""
    # Base case where items list is empty.
    if items == []:
        return None

    # Construct a linked list by traversing the items list through the recursion via
    # slicing, where the 0th element changes at every recursive frame.
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Given a linked list and an int factor, return the list scaled by the factor."""
    # Base case where the linked list is None.
    if head is None:
        return None
    # Construct a linked list where the values are scaled by the int factor.
    # Recursive case returns new nodes until the end of the linked list.
    return Node(head.value * factor, scale(head.next, factor))
