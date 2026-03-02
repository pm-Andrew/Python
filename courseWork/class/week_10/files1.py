# files1.py
# Andrew

import csv
# open the CSV file and assign to variable file
with open("data.csv", newline='') as file:
    # use the CSV reader to read in the CSV file
    reader = csv.reader(file)
    # reads in a line from the reader w/o header
    next(reader)
    # Interarte through the data one row at a time
    for row in reader:
        print(row[2])
try:
