# # Module 3 Skill Building Exercise No. 2 m3-sb2.py
# Andrew

"""
Write a program that uses a `while` loop to determine how long an investment can double at a given interest rate.
The input will be an annualized interest rate, and the output is the years it takes an investment to double.
Note: the initial investment amount does not matter; you can use $1.
"""

def main():
    # get input of intrest rate in float form
    interest = float(int("What is annual rate? "))
    invest = 1
    years = 0

    # while loop that outputs years to double
