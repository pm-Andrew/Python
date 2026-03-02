# fizzbuzz.py

# Common interiew question 

"""
Testing: test_fizzbuzz.py

Students should write tests that:
	•	Verify fizzbuzz(3) returns "Fizz"
	•	Verify fizzbuzz(5) returns "Buzz"
	•	Verify fizzbuzz(15) returns "FizzBuzz"
	•	Verify fizzbuzz(7) returns 7
"""


def fizzbuzz(n):
    """Return 'Fizz' if divisible by 3, 'Buzz' if divisible by 5, 'FizzBuzz' if both, else return n."""
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return n
