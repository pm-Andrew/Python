# test_plates.py
# Andrew

from plates import is_valid


def test_is_valid_beginning_alpha():
    """ test_plates catches plates.py without beginning alphabetical checks """
    assert is_valid("50") == False


def test_is_valid_no_length_check():
    """ test_plates catches plates.py without length checks """
    assert is_valid("CS50500") == False


def test_is_valid_no_number_placement():
    """ test_plates catches plates.py without checks for number placement """
    assert is_valid("CS123A") == False


def test_is_valid_zero_placement():
    """ test_plates catches plates.py without checks for zero placement """
    assert is_valid("CS05") == False


def test_is_valid_no_alpha():
    """ test_plates catches plates.py without checks for alphanumeric characters """
    assert is_valid("AB+-!") != True
