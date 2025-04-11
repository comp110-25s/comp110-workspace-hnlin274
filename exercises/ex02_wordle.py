"""Wordle"""

__author__: str = "730667731"


def contains_char(secret_word: str, single_character: str) -> bool:
    """Determining if the length matches for any index."""
    assert len(single_character) == 1, f"len('{single_character}') is not 1"
    for index in range(len(secret_word)):
        if secret_word[index] == single_character:
            return True
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    emoji_result = ""
    index = 0
    while index < len(secret):
        if guess[index] == secret[index]:
            emoji_result += GREEN_BOX
        else:
            if contains_char(secret, guess[index]) is True:
                emoji_result += YELLOW_BOX
            else:
                emoji_result += WHITE_BOX
        index += 1
    return emoji_result


def input_guess(expected_length: int) -> str:
    """Letting users guess based off the letter count"""
    guess = input(f"Enter a {expected_length} character word:")
    while len(guess) != expected_length:
        if len(guess) < expected_length or len(guess) > expected_length:
            guess = input(f"That wasn't {expected_length} chars! Try again:")
    return guess


def main(secret_word: str) -> None:
    """The entrypoint of the program and the main game loop."""
    guess = ""
    tries = 1
    while guess != secret_word:
        print(f"=== Turn {tries}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if tries <= 6 and guess != secret_word:
            tries += 1
        if tries >= 1 and guess == secret_word:
            print(f" You won in {tries}/6 turns!")
            guess = secret_word
        if tries > 6:
            print("X/6 - Sorry, try again tomorrow!")
            guess = secret_word


if __name__ == "__main__":
    main(secret_word="codes")
