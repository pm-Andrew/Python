# Module 4 Skill-Building Exercise 6
# Andrew


# July 2, 2022 > 2022-07-02

# declare months which has a value of each of the 12 months of the year
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


# Get date from user in m/d/yyyy format
date = input("Enter a date in 'Month Day, Year' format: ")

# Use split to bust apart the date using the space
month,day,year = date.split(" ")

# The day variable has the , as part of it. Strip it off!
day = day.strip(",")

# Now we have month, day and year as strings that we can work with
# But we need to first determine the number of the month using the list
# This will give us a number. We need to add one to it since Python Lists are indexed
# starting at 0. Add one to it to get the month number
monthPosition = months.index(month) + 1

# Since monthPosition is a number, we need to convert it back into a string
# so we can use the zfill() string method
monthPosition = str(monthPosition)

# Print the date with leading 0's for month and day
print(f"{year}-{monthPosition.zfill(2)}-{day.zfill(2)}")
