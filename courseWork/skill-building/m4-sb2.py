# Module 4 Skill-Building Exercise 2 m4-sb2.py
# Andrew

"""
Ask a user to enter a fraction such as 5/10
If the user does not enter a fraction, prompt them again to enter one
"""

def main():
    while True:
        # Ask for a fraction
        fraction = input("Please enter a fraction #/#: \n")

        # if '/' not entered in input
        if "/" in fraction:
            break # stop the loop
        else: # if its not a fraction 
            continue # keep it going

    # Confirmation of fraction
    print(fraction,"is a fraction!!")


main()
