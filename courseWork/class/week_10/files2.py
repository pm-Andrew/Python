# files2.py
# Andrew

import csv

with open("data.csv", newline='') as file:
    # use the csv.DictReader to read in the csv data
    reader = csv.DictReader(file)
    # iterating through the reader one row at a time
    for row in reader:
        print(row["first"])
