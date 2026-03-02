# calculator.py

"""
Testing: test_calculator.py

Students should write tests that:
	•	Verify add(2, 3) returns 5
	•	Verify subtract(10, 5) returns 5
	•	Verify multiply(3, 4) returns 12
	•	Verify divide(10, 2) returns 5.0
	•	Check if divide(5, 0) raises a ValueError
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
