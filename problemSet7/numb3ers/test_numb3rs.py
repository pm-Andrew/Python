# test_numb3rs.py
# Andrew

from numb3rs import validate


def test_validate():
    ''' Valid IP '''
    assert validate("255.255.255.255") == True


def test_validate_false():
    ''' Valid range '''
    assert validate("256.256.256.256") != True


def test_validate_all():
    ''' All Valid Numbers '''
    assert validate("255.256.256.256") != True
