# m8_sb1.py
# Andrew

import re
import sys

"""
Valid stadium seating sections:
XXX.XXX.YY
where XXX is a number between 0 and 255
where YY is two letters

Examples:
123.222.AG is valid
123.222.A is not valid
AAA.BBB.22 is not valid
"""

def main():
    result = validate(input("Enter section number: "))
    if result:
        print(result)
    else:
        sys.exit("Invalid section entered")

def validate(section):
    if re.match(
        r"^(([0-9]|[0-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){2}([A-Z]{2})$",
        section,
        re.IGNORECASE,
    ):
        return "Valid section number entered"
    else:
        return "Invalid section number entered"

if __name__ == "__main__":
    main()
