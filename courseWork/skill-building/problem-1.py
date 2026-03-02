# Problem 1 mod 1
# Andrew

"""
Add two comments to the top of your program, one with the name of the file and the other your name
Create a program that asks a user to enter a sentence.
Using the sentence, print out the sentence in all upper case, all lowercase, and title case
Test your program to make sure it works correctly. Troubleshoot accordingly.
"""

ask = input("Can you please input a sentence? \n").upper()
ask_2 = ask.lower()
ask_3 = ask.title()
print()
print(f"{ask}")
print(f"{ask_2}")
print(f"{ask_3}")
