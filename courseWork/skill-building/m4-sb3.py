# Module 4 Skill-Building Exercise 3 m4-sb3.py
# Andrew


"""
Ask a user to enter a fraction such as 5/10
If the user does not enter a fraction, prompt them again to enter one
Once you get a fraction, ensure the numerator and denominator are numeric. If not, prompt them to enter a new fraction.

"""
def main():
    while True:
        # Ask for a fraction
        fraction = input("Please enter a fraction: \n")

        # if '/' not entered in input
        if "/" in fraction:
            try: # splitting at '/' then checking if #
                num, denom = fraction.split("/")
                num = int(num)
                denom = int(denom)
            except ValueError: # non-int input flag and loop
                continue

            else: # if its a fraction stop
                break

    # Confirmation of fraction
    print(fraction,"is a fraction!!")


main()
