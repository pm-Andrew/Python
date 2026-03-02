# test_find_treasure.py


from game import find_treasure


def test_find_treasure():
    possible_treasures = {"gold coins", "a magic potion", "an ancient key", "a shiny gem"}
    treasure, effect = find_treasure()
    assert treasure in possible_treasures  # Ensures valid treasure
    assert isinstance(effect, str)  # Ensures effect is a string
