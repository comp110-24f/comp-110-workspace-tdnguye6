"""Practicing boolean expressions and conditional statements for CL07"""


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return str("match!")
    else:
        return str("no match!")
