# capture groups.py
# Andrew

import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main():
    # ?P<name> is naming the capture group
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern, number)
    if match:
        # match.group is calling on the capture group named country_code
        country_code = match.group("country_code")
        # print out the location of the country_code
        print(locations[country_code])
    else:
        print("Invalid")
main()
