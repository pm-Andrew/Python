# m7_sb1.py
# How many lines of stock data are there in that file?

try:
    # open a file named data.txt for reading
    file = open("data.txt", "r")
    # use the count variable as a counter
    count = 0
    # iterate through each line in the file
    for line in file:
        # check to see if line is blank and does not start with a ~
        if line.lstrip() != "" and not line.lstrip().startswith("~"):
            # increment the count by one
            count += 1
    print(count)
# catch a file not found error
except OSError as e:
    print("The data.txt file does not exist")
