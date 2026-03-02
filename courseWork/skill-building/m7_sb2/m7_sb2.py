# m7_sb2.py
# Andrew

# import libraries
#  pip install tabulate
import tabulate

# csv is built-in to python
import csv


def process_data(file):
    # open the file as csv.file
    with open(file, newline="") as csv.file:
        # use the csv reader method to read on all of the data from the CSV file
        reader = csv.reader(csv.file,delimiter=",")
        # the first line of the data contains the header
        header = next(reader)
        # create an empty list to store data
        # the list will be used by the tabulate library
        data = []
        for row in reader:
            data.append(row)
        print(tabulate.tabulate(data,header, tablefmt="simple_grid"))

def main():
    # call the process_data() function with the name of the file you want to process
    process_data("data.csv")

if __name__ == "__main__":
    main()
