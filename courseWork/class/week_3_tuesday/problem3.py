# problem3.py
# Convert Minutes to Seconds

"""
Write a function called `minutes_to_seconds` that:
1. Takes one argument: `minutes`.
2. Returns the equivalent number of seconds.

Ask the user for the number of minutes, call the function, and print the result as:
`<minutes> minutes is equal to <seconds> seconds.`
"""

# create function
def minutes_to_seconds(minutes):
    # seconds to minutes
    seconds = minutes * 60
    # returning minutes to seconds
    return seconds

def main():
    # asking for user input
    minutes = int(input("How many hours have you been waiting? "))
    # calling back minutes_to_seconds(minutes) function
    seconds = minutes_to_seconds(minutes)
    # Print out results
    print(f"{minutes} minutes is equal to {seconds} seconds.")


main()




# Output:
# How many hours have you been waiting? 3
# 3 minutes is equal to 180 seconds.


"""
------- No Return ---------
     # Input & argument
    minutes = int(input("Hours to mintues machine!"))
    seconds = minutes * 60

    # Print Function
    print(f"{minutes} minutes is equal to {seconds} seconds.")


# call function
minutes_to_seconds()
"""


