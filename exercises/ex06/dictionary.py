"""Dictionary utilities functions for EX06"""

__author__: str = "730766559"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of key-value pairs of strings, return the same dictionary
    with the keys and values switched.
    """
    # Instantiate a dictionary to be populated with the inverted key-value pairs from
    # input.
    inv_dict: dict[str, str] = {}
    # Instantiate a list of strings to be populated with the keys of the input dict.
    keys_list: list[str] = []
    # Instantiate a list of strings to be populated with the values of the input dict.
    values_list: list[str] = []

    # Populate the keys_list and values_list.
    for keys in input:
        keys_list.append(keys)
        values_list.append(input[keys])

    # Iterate over the values_list and raise a KeyError if duplicate values are found
    # to avoid unexpected behavior when inverting the input dict.
    vals_idx: int = 0
    while vals_idx < len(values_list) - 1:
        if values_list[vals_idx] == values_list[vals_idx + 1]:
            raise KeyError("Input cannot have duplicate values in order to invert.")
        vals_idx += 1

    # Raise a KeyError if a duplicate key is found in keys_list.
    keys_idx: int = 0
    while keys_idx < len(keys_list) - 1:
        if keys_list[keys_idx] == keys_list[keys_idx + 1]:
            raise KeyError("Input cannot have duplicate keys.")
        keys_idx += 1

    # Iterate over the length of the input dict to populate the inverted dict with the values
    # in values_list as the keys and the keys in keys_list as the values.
    for inv_keys_idx in range(0, len(input)):
        inv_dict[values_list[inv_keys_idx]] = keys_list[inv_keys_idx]

    return inv_dict


def favorite_color(input: dict[str, str]) -> str:
    """Given a dict input with the names of people as keys and their favorite color as the
    pairing value, then count the number of times every unique color is chosen and return
    the color with the highest number of appearances in input.
    """
    # Instantiate a dictionary holding key-value pairs of unique colors and the number
    # of times it appears in the input.
    fav_color_count: dict[str, int] = {}
    # Initialize an int variable that will be updated as the maximum number
    # of appearances of any given color increases.
    max: int = 0
    # Initialize a str variable that will be updated as the color whose number of
    # appearances matches the max variable
    best_color: str = ""
    # Iterate over the entire input dict and populate fav_color_count with
    # keys corresponding to unique colors appearing in the input. If a
    # duplicate value (i.e., a repeated color) is encountered,
    # simply add 1 to the total number of appearances in the
    # fav_color_count dict.
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
    """Given an input list of strings, return a dictionary populated
    with every uniquely appearing string as keys and the number of times
    such a string is repeated in the input.
    """
    # Instantiate a dictionary that will contain every unique string
    # as keys and the number of appearances as their values.
    count_dict: dict[str, int] = {}

    # Iterate over the input list and populate count_dict with every unique
    # string, or if it already exists as a key, add one to the key's value.
    for string in input:
        if string in count_dict:
            count_dict[string] += 1
        else:
            count_dict[string] = 1

    return count_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Given a list of words, return a dictionary whose keys are all the unique
    first letters that appear in the list and values are lists of words in the given
    list whose first letters correspond to the keys.
    """
    # Instantiate a dictionary to be populated with keys as
    # the unique first letters of the input and lists of words
    # containing that first letter corresponding to the keys as the values.
    similar_words: dict[str, list[str]] = {}
    # Iterate over the given list of words.
    for word in words:
        if word != "":  # Address user misbehavior of empty strings in the given list.
            # Dynamically update the first_letter encountered over the
            # words list, using .lower() method to distinguish from
            # the original string in words list to be added to the
            # similar_words dict.
            first_letter = word[0].lower()
            # Populate similar_words with every unique first letter and an
            # empty string.
            if first_letter not in similar_words:
                similar_words[first_letter] = []
            # So long as a word in the given words list is not an empty string,
            # add the word to the list corresponding to the unique first letter
            # key.
            similar_words[first_letter].append(word)
    return similar_words


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Given an attendance_log dictionary with days of the week as
    keys and a str list of students that attended class on that day
    as the values, given a day of the week, and given a student, mutate
    the given attendance_log dictionary by adding the given day of the
    week and the student that attended class for that given day.
    """
    # Main use case where the day is not already in the attendance_log.
    if day not in attendance_log:
        attendance_log[day] = []  # Populate attendance_log with day and empty list.
    # Populate list of present students for given day with given student.
    if student not in attendance_log[day]:
        attendance_log[day].append(student)
