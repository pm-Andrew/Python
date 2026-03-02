# Problem 4: Outdated outdated.py
# Andrew

# 2/11/2025 2025-02-11
# 7/2/1963 1963-07-02

# February 11, 2025
# 2025-02-11

# July 2, 1693
# 1936-07-02

def main():
    # forever loop until
    while True:
        # grab date from user
        date = input("Date: ")

        # determine which date format we have
        # is it / or the one with the , in it
        if "/" in date:
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
                    continue
                # check day
                if day < 1 or day > 31:
                    continue
                # check year
                if year < 0:
                    continue
                # printing in the form YYYY-MM-DD
                print(f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}")
                break

            except ValueError:
                continue

        # checking if in ad date format
        if "," in date:
            months = [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
            ]

            # Splitting by blank space
            # February 14, 2025
            month, day, year = date.split(" ")
            try:
                # stripping off the "," part of day
                day = day.strip(",")
                day = int(day)
                # changing positions in dict
                monthNum = months.index(month) + 1

                # check day
                if day < 1 or day > 31:
                    continue
                # check month
                if monthNum < 1 or monthNum > 12:
                    continue

                # 07/02/1963 > 1963/07/02
                print(f"{year}-{str(monthNum).zfill(2)}-{str(day).zfill(2)}")
                break
            # continue if input is not valid
            except ValueError:
                continue


main()
