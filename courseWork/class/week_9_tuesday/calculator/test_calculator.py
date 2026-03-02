# test_calculator.py
# Andrew


import pytest
from calculator import add, subtract, multiply, divide

"""
Testing: test_calculator.py

Students should write tests that:
	•	Verify add(2, 3) returns 5
	•	Verify subtract(10, 5) returns 5
	•	Verify multiply(3, 4) returns 12
	•	Verify divide(10, 2) returns 5.0
	•	Check if divide(5, 0) raises a ValueError
"""

def test_add():
    assert add(2,3) == 5
    assert add(2,0) == 2
    assert add(0,0) == 0
    assert add(-2,-3) == -5

def test_subtract():
    assert subtract(10,5) == 5

def test_multiply():
    assert multiply(3,4) == 12

def test_divide():
    assert divide(10,2) == 5.0

def test_divide_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)
