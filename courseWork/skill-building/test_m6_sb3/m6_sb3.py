# Module 6 Skill-Building Exercise 3
# Andrew

def main():
    # asking user for fraction
    fraction = input("Fraction: ")
    # calling convert
    percentage = convert(fraction)
    # print results
    print(percentage)

def convert(fraction):
    # use simultaneous assignment to get numerator and denominator
    # splitting the fractions and assigning x,y as variables
    x, y = fraction.split("/")
    try:
        # numberator is a number?
        x = int(x)
        # denominator is a number?
        y = int(y)
        # if undefined fraction raise an error message
        if y == 0:
            # if so raise error message
            raise ZeroDivisionError("It appears the denominator is 0")
        else:
            # if pass return as a percentage
            return int((x/y) * 100)
    # error message if numerator or denominator or both are not numeric
    except ValueError:
        raise ValueError("Invalid fraction")

if __name__ == "__main__":
    main()


