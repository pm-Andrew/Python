# lines2.py
# Andrew

# used to track numbers of code
count = 0

# open the file you need to count the code in
with open("adieu.py", "r") as file:
    # Start with while loop that counts the lines
    for line in file:
        line = line.strip()

        # write a check to see if thers is a # at the start of line if there is don't count it
        if line.startswith("#"):
            continue

        # if line contains a letter in that of the line count it
        if line == "":
            continue
        count = count + 1

print(count)

