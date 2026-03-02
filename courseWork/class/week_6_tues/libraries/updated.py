# Problem 4: Outdated updated.py
# Andrew

def slash_date(date):
    # we need to split the parts into month, day, year
    # taking str input and changing to integers
    try:
        # Splitting by "/"
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)

        # check month
        if month < 1 or month > 12:
            return False
        # check day
        if day < 1 or day > 31:
            return False
        # check year
        if year < 0:
            return False
        # printing in the form YYYY-MM-DD
        print(f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}")
        return True

    except ValueError:
        return False


def comma_date(date):
    months = {
        "January": 1,
        "February": 2,
                "March": 3,
                "April": 4,
                "May": 5,
                "June": 6,
                "July": 7,
                "August": 8,
                "September": 9,
                "October": 10,
                "November": 11,
                "December": 12,
    }

    # Splitting by blank space
      # February 14, 2025
    month, day, year = date.split(" ")
    try:
        # stripping off the "," part of day
        day = day.strip(",")
        day = int(day)
        # changing positions in dict
        # monthNum = months.index(month) + 1
        monthNum = months[month]

        # check day
        if day < 1 or day > 31:
            return False
        # check month
        if monthNum < 1 or monthNum > 12:
            return False

        # 07/02/1963 > 1963/07/02
        print(f"{year}-{str(monthNum).zfill(2)}-{str(day).zfill(2)}")
        return True
    # continue if input is not valid
    except (ValueError, KeyError):
        return False


def main():
    # forever loop until
    while True:
        # grab date from user
        date = input("Date: ").title()

        # determine which date format we have
        # is it / or the one with the , in it
        if "/" in date:
            result = slash_date(date)

            if result:
                break
            else:
                continue

        # checking if in ad date format
        elif "," in date:
            result = comma_date(date)

            if result:
                break
            else:
                continue


main()
