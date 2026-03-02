# working.py
# Andrew


import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # searching for the time in 12hr
    timeGroups = re.search(
        r"^([1-9]|[1][0-2])(?:\:([0-5][\d]))?\s([aApP][mM])\sto\s([1-9]|[1][0-2])(?:\:([0-5]\d))?\s([aApP][mM])$", s, re.IGNORECASE)

    # if valid input is entered
    if timeGroups != None:
        # First times hour entered in correctly
        # am is 00-12 and has am or AM in it
        if timeGroups.group(1) == "12" and timeGroups.group(3).lower() == "am":
            firstTime = "00"
        # if < 12 and has pm or PM in it
        elif int(timeGroups.group(1)) < 12 and timeGroups.group(3).lower() == "pm":
            # turning a int into a str while converting 12hr to 24hr formatting
            firstTime = str(int(timeGroups.group(1)) + 12).zfill(2)
        else:
            # entered 24 hr
            firstTime = timeGroups.group(1).zfill(2)

        # First times minutes
        if timeGroups.group(2) != None:
            # 00-60
            firstTime = firstTime + f":{timeGroups.group(2).zfill(2)}"
        else:
            # 00-60
            firstTime = f"{firstTime}:00"

        # Second times hour
        # am is 00-12 and has am or AM in it
        if (timeGroups.group(4) == "12" and timeGroups.group(6).lower() == "am" and (timeGroups.group(5) == None or timeGroups.group(5) == "00")):
            secondTime == "00"
        # if < 12 and has pm or PM in it
        elif int(timeGroups.group(4)) < 12 and timeGroups.group(6).lower() == "pm":
            # turning a int into a str while converting 12hr to 24hr formatting
            secondTime = str(int(timeGroups.group(4)) + 12).zfill(2)
        else:
            secondTime = timeGroups.group(4).zfill(2)

        # Second times minutes
        if timeGroups.group(5) != None:
            # 00-60
            secondTime += f":{timeGroups.group(5).zfill(2)}"
        else:
            # 00-60
            secondTime = f"{secondTime}:00"
        return f"{firstTime} to {secondTime}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
