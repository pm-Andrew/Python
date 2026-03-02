# seasons.py
# Andrew S

import inflect
import sys
from datetime import date


# converting dob & today
def calc(dob):

    NUMBER_OF_MINUTES_IN_DAY  = 1440

    try:
        # get year, month and day from dob string
        year, month, day = dob.split("-")
        # convert the string into a date
        result = date(int(year), int(month), int(day))
        # get todays date
        today = date.today()
        # calculate difference and use days property
        days = (today - result).days
        # calculate number of minutes for the number of days
        minutes = days * NUMBER_OF_MINUTES_IN_DAY

        # creating an inflect engine instance for converting
        p = inflect.engine()
        # return the formatted string
        return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"
    except ValueError:
        raise ValueError


def main():

    try:
        # getting users D.O.B
        dob = input("Date of Birth: ")
        # expect date format YYYY-MM-DD
        # Call the calc function with dob
        diff = calc(dob)
        # print minutes
        print(diff)
    except ValueError:
        sys.exit("Invalid Date")


if __name__ == "__main__":
    main()
