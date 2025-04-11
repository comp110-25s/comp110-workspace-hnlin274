"""Unit Tests for Dictionary Functions!"""

__author__: str = "730667731"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len
import pytest


def test_invert_use_case() -> None:
    """Tests a common use case for invert."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_edge_case() -> None:
    """Tests an edge case for invert with empty dictionary."""
    assert invert({}) == {}


def test_invert_key_error() -> None:
    """Tests that KeyError is raised for duplicate values when inverting."""
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


def test_favorite_color_use_case() -> None:
    """Tests a common use case for favorite_color."""
    assert favorite_color({"Alice": "blue", "Bob": "red", "Charlie": "blue"}) == "blue"


def test_favorite_color_edge_case() -> None:
    """Tests an edge case with an empty dictionary."""
    assert favorite_color({}) == ""


def test_favorite_color_tie() -> None:
    """Tests a case where there is a tie, returning first encountered color."""
    assert (
        favorite_color(
            {"Alice": "blue", "Bob": "red", "Charlie": "red", "Dave": "blue"}
        )
        == "blue"
    )


def test_count_use_case() -> None:
    """Tests a common use case for count."""
    assert count(["apple", "banana", "apple", "cherry", "banana", "banana"]) == {
        "apple": 2,
        "banana": 3,
        "cherry": 1,
    }


def test_count_edge_case() -> None:
    """Tests an edge case with an empty list."""
    assert count([]) == {}


def test_count_single_item() -> None:
    """Tests a case with a single unique item repeated."""
    assert count(["apple", "apple", "apple"]) == {"apple": 3}


def test_bin_len_use_case() -> None:
    """Tests a common use case for bin_len."""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_edge_case() -> None:
    """Tests an edge case with an empty list."""
    assert bin_len([]) == {}


def test_bin_len_duplicate_length() -> None:
    """Tests a case with multiple words of the same length."""
    assert bin_len(["dog", "cat", "bat"]) == {3: {"dog", "cat", "bat"}}
