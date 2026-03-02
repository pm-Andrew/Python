# palindrone.py

"""
Testing: test_palindrome.py

Students should write tests that:
	•	Verify is_palindrome("racecar") returns True
	•	Verify is_palindrome("hello") returns False
	•	Verify is_palindrome("A man a plan a canal Panama") returns True
	•	Test an empty string and a single-character string
"""


def is_palindrome(s):
    """Check if a string is a palindrome (ignoring case and spaces)."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]
