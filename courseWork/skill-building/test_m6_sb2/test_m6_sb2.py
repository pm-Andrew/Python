# test_m6_sb2.py
# Andrew

# importing value() from m6_sb2
from m6_sb2 import value

def test_bad_feedback():
    # testing if other values outputs correctly
    assert value("poor") == "All feedback is good feedback"


def test_case_insensitivity():
    # testing if good values outputs correctly
    assert value("GOOD") == "Thank you for that good rating"


def test_excellent_feedback():
    # testing if execellent values outputs correctly
    assert value("exCELLENT") == "Thank you for an excellent rating"
