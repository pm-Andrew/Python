# um.py
# Andrew


import re
import sys

# House main logic
def main():
    print(count(input("Text: ")))

# start count at zeero
count = 0

# takings and find umUM in input
def count(s):
    # regex used narrows down to only umUM and not words like umberlla...etc
    count = re.findall(r"\b(?:(um)|(UM))\b", s, re.IGNORECASE)
    # return the count of um
    return len(count)


if __name__ == "__main__":
    main()
