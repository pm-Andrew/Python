# test_working.py
# Andrew


from working import convert
import pytest

def test_convert_correct_time():
    ''' Correct formatting '''
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_convert_incorrect_hours():
    ''' Invalid Hours '''
    with pytest.raises(ValueError):
        convert("23 AM to 8 PM")

def test_convert_incorrect_mintues():
    ''' Invalid Minutes '''
    with pytest.raises(ValueError):
        convert("12:99 AM to 5 PM")

def test_convert_no_to():
    ''' Missing to '''
    with pytest.raises(ValueError):
        convert("11 AM 9 PM")

def test_convert_invalid_time_format():
    ''' Missing am/pm '''
    with pytest.raises(ValueError):
        convert("8 AM to 12")
