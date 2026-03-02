# lines.py
# Andrew

import sys

# need to check that they type in a file after the python lines.py______
if len(sys.argv) != 2:
    # asking for '$ python lines.py adieu.py'
    sys.exit("Too few command-line arguments")

# now we need to ensure that file is a python file (.py)
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

# and we need to check that it actually is a real file

# used to track numbers of code
count = 0

try:
    # open the file you need to count the code in
    with open(sys.argv[1], "r") as file:
        # Start with while loop that counts the lines
        for line in file:

            # srtip off any spaces, tabs, or lines feeds
            line = line.strip()
            # write a check to see if thers is a # at the start of line if there is don't count it
            if line.startswith("#"):
                continue

            # if line contains a letter in that of the line count it
            if line == "":
                continue

            count = count + 1
            
except FileNotFoundError:
    sys.exit("File not Found")

print(count)

