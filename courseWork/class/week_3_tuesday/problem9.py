9  # problem9.py
# Full Name Formatter


"""
Write a function called `format_name` that:
1. Takes two arguments: `first_name` and `last_name`.
2. Returns the full name in the format: `<Last Name>, <First Name>`.

Ask the user for their first and last names, call the function, and print the formatted result.

Example:
Enter your first name: Bruce
Enter your last name: Elgort
Output: Elgort, Bruce
"""


# define 'format_name' that takes `first_name` and `last_name` and swaps order
def format_name(first_name, last_name):
    # rearraging name
    return last_name + "," + first_name
    # return f"{last_name}, {first_name}


def main():
    # ask for user input
    first_name = input("What is your first name? ").capitalize()
    last_name = input("What is your last name? ").capitalize()
    new_name = format_name(first_name, last_name)
    # print results
    print(new_name)


main()


# Output:
# What is your first name? zone
# What is your last name? danger
# Danger,Zone
