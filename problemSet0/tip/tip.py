# Tip Calculator tip.py
# Andrew S

# User input and tip formula
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# covert dollars from $10 to a float 10.00 (decimal)
def dollars_to_float(d):
    # strip the $
    d = d.strip("$")
    # turn into a float
    d = float(d)
    # return value
    return d


def percent_to_float(p):
    # convert percent to a float (decimal)
    p = p.strip("%")
    # float to a decimal
    p = float(p) / 100
    # return value
    return p


main()
