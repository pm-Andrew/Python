# Module 4 Skill-Building Exercise 4 m4-sb4.py
# Andrew


"""
Create a dictionary of course numbers (ie, CTEC 121, CTEC 122, etc.) and their associated number of credits.
Write a program that asks a user to enter the course they want to take
Accumulate the total number of course credits using the dictionary
Once the user pressed control+d on their keyboard, display the total number of credits
"""


def main():
    courses = { # List of courses
        "CTEC 121": 5,
        "CTEC 122": 4,
        "CTEC 126": 5,
        "CTEC 127": 5,
        "CTEC 145": 5,
        "CTEC 227": 5,
        "CTEC 270": 5,
    }

    credits = 0 # variable for total credits

    while True: # forever loop
        try:
            # User input
            course = input("Which course would you like to take: ").upper()
            # call course from dict
            if course in courses:
                credits = credits + courses[course]
        # ctrl + d error
        except EOFError:
            # end loop
            break
        print(f"The total number of credits taking: {credits}")


main()
