# functions.py
# Andrew S


def convert_tip_percentage(tip):
    # remove the %
    tip = tip.strip("%")
    # convert to the float and the decimal
    tip = float(tip) / 100
    # return the value of tip
    return tip


def main():
    # define cost of dinner
    meal_cost = 35.22  # Hard coding
    # get tip amount including % from user
    tip_amount = input("Enter a tip amout: ")
    # convert tip amount
    tip_percentage = convert_tip_percentage(tip_amount)
    # calculate meal total
    tip_amount = meal_cost * tip_percentage
    # display results
    print(f"The total cost of the meal was ${meal_cost + tip_amount:,.2f}")


main()
