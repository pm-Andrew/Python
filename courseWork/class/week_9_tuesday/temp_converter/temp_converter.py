# temp_converter.py

"""
Testing: test_temperature.py

Students should write tests that:
	•	Check if celsius_to_fahrenheit(0) returns 32
	•	Check if fahrenheit_to_celsius(32) returns 0
	•	Test edge cases like 100 Celsius or -40 (where both scales are equal)

Place your tests in a file named test_temp_converter.py
"""


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def main():
    print(f"0 degrees Celsius is {celsius_to_fahrenheit(0)} degrees Fahrenheit")
    print(f"32 degrees Fahrenheit is {fahrenheit_to_celsius(32)} degrees Celsius")


if __name__ == "__main__":
    main()
