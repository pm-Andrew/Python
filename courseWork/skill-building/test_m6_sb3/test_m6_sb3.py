# test_m6_sb3.py
# Andrew

# importing convert()
from m6_sb3 import convert
# import pytest library
import pytest

# testing invalid fractions
def test_convert_valueError():
    # see if pytest raises a ValueError
    with pytest.raises(ValueError) as excinfo:
        # call the convert function with "a/b"
        convert("a/b")
        # assert that an error has occurred
        assert "Incorrect values in fraction"

# testing undefined fractions
def test_convert_undefined():
    with pytest.raises(ZeroDivisionError) as excinfo:
        # call the convert with "1/0"
        convert("1/0")
        # assert that an error has occurred
        assert "The fraction contained a 0 in the denominator"
