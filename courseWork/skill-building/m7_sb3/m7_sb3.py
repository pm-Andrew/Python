# m7_sb3.py
# Andrew

# m7_sb3.py
# Andrew

# This example will help you with the Scourgify problem in Problem Set 7
# The file names are hardcoded in this example
# Your code will require that you process arguments from the command line
# Also, please be sure to change variable names and other code to solve
# the Scourgify problem.
# I also ask that you don't use my comments but reword your own

import csv

def process_csv_data(inputFile,outputFile):
    # open the file
    with open (inputFile) as before:
        # use csv.reader to read the data
        # seprating by "," & groups with '"'
        data = csv.reader(before, delimiter=",", quotechar='"')
        # Skipping the header
        next(data)

        # create and open after.py
        with open(outputFile, "w", newline="") as after:
            # Header row
            fieldNames =["first", "last", "course", "major"]
            # CSV DictWriter to create file
            writer = csv.DictWriter(after, fieldnames=fieldNames)

            # Add header to the top
            writer.writeheader()

            # Iterate throught the data read in via csv.reader
            for row in data:
                #
                #
                name = row[0]
                #
                #
                last, first = name.split(",")
                #
                course = row[1]
                #
                major = row[2]
                #
                writer.writerow(
                    {"first": first, "last": last, "course": course, "major": major}
                )

def main():
    #
    inputFile = "before.csv"
    #
    outputFile = "after.csv"
    #
    process_csv_data(inputFile, outputFile)

if __name__ == "__main__":
    main()


