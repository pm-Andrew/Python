# test_bank.py
# Andrew


from bank import value


def test_value_incorrect():
    """ incorrect values outputted """
    assert value("hello") == 0


def test_no_case_error():
    """ Without case-insensitivity """
    assert value("HELLO") == 0


def test_noHello():
    """ not allowing full phrase """
    assert value("HE") == 20
