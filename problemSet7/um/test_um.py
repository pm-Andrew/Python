# test_um.py
# Andrew
from um import count


def test_um_count_noTum():
    assert count(" um ") == True


def test_um_count_noDrum():
    assert count("Drum") != True


def test_um_count():
    assert count("Um") == True
