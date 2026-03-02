# pattern.py
# Andrew

import re


def main():
    code = input("Hexadecimal color code: ")

    # ^ = starts with #, $ = ends with [a-fA-F0-9] range, with only 6 characters
    pattern = r"^#[a-fA-F0-9]{6}$"
    # using search function
    match = re.search(pattern, code)
    # if there is a match
    if match:
        print(f"Valid. Matched with {match.group()}")
    # Not a match
    else:
        print("Invalid")

main()
