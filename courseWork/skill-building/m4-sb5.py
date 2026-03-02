# Module 4 Skill-Building Exercise 5 m4-sb5.py
# Andrew

"""
Has a user enter a day in m/d/yyyy format
If the user enters the month or day as 1-9 or 1-9 make sure to print it out with a leading 0, such as 01, 02, 03, etc.
Print out the newly formatted date
"""

# input
date = input("Date in m/d/yyyy: ")

# split date
month, day, year = date.split("/")

# print out
print(f"{month.zfill(2)}/{day.zfill(2)}/{year}")



