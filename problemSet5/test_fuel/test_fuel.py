# test_fuel.py
# Andrew

import pytest
from fuel import convert, gauge


def test_convert_valid_function():
    """ valid function """
    assert convert("1/4") == 25


def test_convert_value_error():
    """ ValueError """
    with pytest.raises(ValueError):
        convert("100/50")


def test_convert_zeroDiv_error():
    """ ZeroDivision """
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_empty():
    """ empty """
    assert gauge(1) == "E"


def test_gauge_no_percent_sign():
    """ no percent """
    assert gauge(50) != "50"


def test_gauge_not_labeling_full():
    """ no label """
    assert gauge(99) == "F"
    assert gauge(99) != "55"
