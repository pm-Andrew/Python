# Scourgify.py
# Andrew

# import libraries
import csv
import sys


def process_csv_data(inputFile, outputFile):
    # open the file
    with open(inputFile, "r") as before:
        # use csv.reader to read the data
        # seprating by "," & groups with '"'
        data = csv.reader(before, delimiter=",", quotechar='"')
        # Skipping the header
        next(data)

        # create and open after.py
        with open(outputFile, "w", newline="") as after:
            # Header row
            fieldNames = ["first", "last", "house"]
            # CSV DictWriter to create file
            writer = csv.DictWriter(after, fieldnames=fieldNames)
            # Add header to the top
            writer.writeheader()

            # Iterate throught the data read in via csv.reader
            for row in data:
                # asign row[0] name
                name = row[0]
                # in before.csv split name
                last, first = name.split(",")
                # Strip any whitespace on first and last
                last = last.strip()
                first = first.strip()
                # assign row[1] house
                house = row[1]
                # assign format of rows in 'after.csv'
                writer.writerow(
                    {"first": first, "last": last, "house": house}
                )


def main():
    try:
        # Too few command-line arguments / no sys arg
        if len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        # Too many command-line arguments
        elif len(sys.argv) == 4:
            sys.exit("Too many command-line arguments")
        # Valid inputs
        # if 'before.csv after.csv' is inputted in command-line
        elif len(sys.argv) == 3:
            # call process_csv_data() and accept arguments
            # program ends when done
            process_csv_data(sys.argv[1], sys.argv[2])
        # Not a CSV file
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        # anything else is not valid
        else:
            sys.exit("Could not read invalid_file.csv")
    # Error handling
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")


if __name__ == "__main__":
    main()
