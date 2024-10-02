"""Wordle programmed in Python"""

__author__: str = "730766559"


def input_guess(secret_word_len: int) -> str:
    """Prompt user for a word of given length as a 'guess' for the secret word"""
    input_word: str = input(f"Enter a {secret_word_len} character word: ")
    # Establish boolean variable as condition for while loop
    valid_guess: bool = True
    # Prompt user for guesses until a word of the correct length is guessed
    while valid_guess == True:
        if len(input_word) != secret_word_len:
            input_word = input(f"That wasn't 5 chars! Try again: ")
        else:
            valid_guess = False
    return input_word


def contains_char(secret_word: str, searched_char: str) -> bool:
    """Check if a given letter is included in the secret word"""
    # Ensure program assumes that searched_char argument is of length 1 and
    # error if otherwise.
    assert len(searched_char) == 1
    # Index variable for condition of while loop
    search_index: int = 0
    # Iterate over secret word. Return true if there is a match. Return false if
    # searched_char does not match any chars of secret_word
    while search_index < len(secret_word):
        if secret_word[search_index] == searched_char:
            return True
        else:
            search_index += 1
    # Only runs if searched_char never matches with secret_word
    if search_index == len(secret_word):
        return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(user_guess: str, secret_word: str) -> str:
    """
    Print the progress of user's wordle using WHITE_BOX, GREEN_BOX, and
    YELLOW_BOX. Instances of WHITE_BOX are determined by no matching chars,
    instances of GREEN_BOX are determined by matching char and index,
    instances of YELLOW_BOX are determined by matching char but non-matching
    index; all based on user's guess.
    """
    # Ensure assumption of matching char len of user_guess and secret_word
    assert len(user_guess) == len(secret_word)
    wordle_index: int = 0
    # Empty string to be populated by progress indicators (white, green, yellow boxes)
    wordle_progress: str = ""
    # Iterate over entire user_guess to determine wordle progress
    while wordle_index < len(user_guess):
        # Verify if char in secret_word matches char in user_guess in same index
        if contains_char(
            secret_word=secret_word, searched_char=user_guess[wordle_index]
        ):
            # Populate "wordle_index"th index of wordle_progress string with GREEN_BOX
            # if matching char and index
            if user_guess[wordle_index] == secret_word[wordle_index]:
                wordle_progress += GREEN_BOX
            # Populate "wordle_index"th index of wordle_progress string with YELLOW_BOX
            # if matching char but not index
            else:
                wordle_progress += YELLOW_BOX
        # Populate "wordle_index"th index of wordle_progress string with WHITE_BOX
        # if no matching char
        else:
            wordle_progress += WHITE_BOX
        # Index into next char of user_guess
        wordle_index += 1
    # Store wordle_progress string
    return wordle_progress


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    current_turn: int = 1
    max_turns: int = len(secret)
    user_guess: str
    while current_turn <= max_turns:
        print(f"=== Turn {current_turn}/{max_turns} ===")
        user_guess = input_guess(len(secret))
        print(emojified(user_guess, secret))
        if user_guess == secret:
            print(f"You won in {current_turn}/{max_turns}!")
            return
        current_turn += 1
    if current_turn == max_turns:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main(secret="codes")
