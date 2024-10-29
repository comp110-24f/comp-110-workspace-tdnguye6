"""Dictionary utilities functions for EX06"""

__author__: str = "730766559"


def invert(input: dict[str, str]) -> dict[str, str]:
    inv_dict: dict[str, str] = {}
    keys_list: list[str] = []
    values_list: list[str] = []

    for keys in input:
        keys_list.append(keys)
        values_list.append(input[keys])

    vals_idx: int = 0
    while vals_idx < len(values_list) - 1:
        if values_list[vals_idx] == values_list[vals_idx + 1]:
            raise KeyError("Input cannot have duplicate values in order to invert.")
        vals_idx += 1

    keys_idx: int = 0
    while keys_idx < len(keys_list) - 1:
        if keys_list[keys_idx] == keys_list[keys_idx + 1]:
            raise KeyError("Input cannot have duplicate keys.")
        keys_idx += 1

    for inv_keys_idx in range(0, len(input)):
        inv_dict[values_list[inv_keys_idx]] = keys_list[inv_keys_idx]

    return inv_dict


def favorite_color(input: dict[str, str]) -> str:
    fav_color_count: dict[str, int] = {}
    max: int = 0
    best_color: str = ""
    for names in input:
        color = input[names]
        if color in fav_color_count:
            fav_color_count[color] += 1
        else:
            fav_color_count[color] = 1

        if fav_color_count[color] > max:
            best_color = color
            max += 1

    return best_color


def count(input: list[str]) -> dict[str, int]:
    count_dict: dict[str, int] = {}

    for string in input:
        if string in count_dict:
            count_dict[string] += 1
        else:
            count_dict[string] = 1

    return count_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    similar_words: dict[str, list[str]] = {}
    for word in words:
        if word != "":
            first_letter = word[0].lower()
            if first_letter not in similar_words:
                similar_words[first_letter] = []
            similar_words[first_letter].append(word)
    return similar_words


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:

    if day not in attendance_log:
        attendance_log[day] = []
    attendance_log[day].append(student)
