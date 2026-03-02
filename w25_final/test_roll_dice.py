# test_roll_dice.py

from game import roll_dice


def test_roll_dice():
    result = roll_dice()
    assert 1 <= result <= 6  # Ensures valid range
    assert isinstance(result, int)  # Ensures it's an integer
