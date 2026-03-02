# test_battle_monster.py

from game import battle_monster


def test_battle_monster():
    assert battle_monster(5, 3, False) is True  # Player wins
    assert battle_monster(2, 5, False) is False  # Player loses
    assert battle_monster(4, 5, True) is True  # Potion boosts attack to win
