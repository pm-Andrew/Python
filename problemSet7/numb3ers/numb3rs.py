# numb3rs.py
# Andrew


import re
import sys


def main():
    result = validate(input("IPv4 Address: "))

    if result == True:
        print(result)
    else:
        sys.exit(1)


def validate(ip):
    if re.match(
            r"^(([0-9]|[0-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
