# demo7.py
# Andrew Sabourin

"""
I want to develop a program that removes a $ from a string

"""


def convert(dollar_amount):
    # replace the $ with ""
    dollar_amount = dollar_amount.replace("$", "")
    # send back value of dollar_amount
    return dollar_amount


def make_float(number):
    return float(number)


# get string input from user including $
cost_of_dinner = input("Enter the cost of dinner: ")
# call the convert function to strip off the $
cost_of_dinner = convert(cost_of_dinner)
# call the make_float function
cost_of_dinner = make_float(cost_of_dinner)
print(type(cost_of_dinner))
# print out result
print(cost_of_dinner)
