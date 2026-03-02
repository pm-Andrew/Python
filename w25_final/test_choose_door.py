# test_choose_door.py


from game import choose_door


def test_choose_door():
    assert choose_door(1, True) is True  # Has key, auto success
    assert choose_door(2, True) is True  # Has key, auto success
    assert choose_door(3, False) is False  # Invalid choice fails
    assert choose_door(1, False) in [True, False]  # Randomized outcome
