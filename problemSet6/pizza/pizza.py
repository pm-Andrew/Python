# pizza.py
# Andrew

import csv
import tabulate
import sys


def pizza_reader(file):
    # open csv files 'regular' & 'sicilian <-------????
    with open(file, newline="") as csv.file:
        # Read the files using csv.reader
        reader = csv.reader(csv.file, delimiter=",")
        # designating first row is a header
        header = next(reader)
        # create a empyt list for tabulate
        data = []
        # each row in csv
        for row in reader:
            # append rows with a header
            data.append(row)
        print(tabulate.tabulate(data, header, tablefmt="grid"))


def main():
    try:
        # Too few command-line arguments / no sys arg
        if len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        # Too many command-line arguments
        elif len(sys.argv) == 3:
            sys.exit("Too many command-line arguments")
        # Valid inputs
        # if 'regular.csv' is inputted in command-line
        elif len(sys.argv) == 2 and sys.argv[1] == "regular.csv":
            # Print Regular
            pizza_reader("regular.csv")
        # if 'sicilian.csv' is inputted command-line
        elif len(sys.argv) == 2 and sys.argv[1] == "sicilian.csv":
            # print Sicilian
            pizza_reader("sicilian.csv")
        # Not a CSV file
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        # invaild command-lines
        else:
            sys.exit("File does not exist")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
