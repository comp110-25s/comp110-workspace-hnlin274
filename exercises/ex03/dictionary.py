"""Unit Tests for Dictionary Functions!"""

__author__: str = "730667731"


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the key-value pairs in the dictionary."""
    output: dict[str, str] = {}
    for key, value in my_dict.items():
        if value in output:
            raise KeyError("Duplicate key found when inverting!")
        output[value] = key
    return output


def favorite_color(my_dict: dict[str, str]) -> str:
    """Returns the most frequent color in the dictionary."""
    color_count: dict[str, int] = {}
    for color in my_dict.values():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    max_color = ""
    max_count = 0
    for color, count in color_count.items():
        if count > max_count:
            max_color = color
            max_count = count
    return max_color


def count(values: list[str]) -> dict[str, int]:
    """Returns a dictionary counting occurrences of each string in the list."""
    output: dict[str, int] = {}
    for item in values:
        if item in output:
            output[item] += 1
        else:
            output[item] = 1
    return output


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Groups words by their length into a dictionary."""
    output: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length in output:
            output[length].add(word)
        else:
            output[length] = {word}
    return output
