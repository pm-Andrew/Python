# test_palindrone.py
# Andrew


"""
Testing: test_palindrome.py

Students should write tests that:
	•	Verify is_palindrome("racecar") returns True
	•	Verify is_palindrome("hello") returns False
	•	Verify is_palindrome("A man a plan a canal Panama") returns True
	•	Test an empty string and a single-character string
"""

from palindrone import is_palindrome

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("") == True
    assert is_palindrome(" ") == True
