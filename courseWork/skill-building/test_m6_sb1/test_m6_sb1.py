# test_m6_sb1.py
# Andrew

from m6_sb1 import shorten

def test_shorten_noSpace():
    # catches no spaces
    assert shorten("I see you") != "I see you"

def test_shorten_case():
    # catches no change to case
    assert shorten("I see you") != "ISEEYOU"

def test_shorten_noNum():
    # Catches numbers
    assert shorten("I see you 56") != "Iseeyou"

def test_shorten_noUpper():
    # catches upper case
    assert shorten("I see you") != "ISEEYOU"

def test_shorten_noPun():
    # catches puncuation
    assert shorten("I see you!") != "ISEEYOU"
