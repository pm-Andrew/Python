# problem2.py
# Calculate the Square

"""
Write a function called `calculate_square` that:
1. Takes one argument: `number`.
2. Returns the square of the number.

Ask the user for a number, call the function, and print the result as:
`The square of <number> is <result>.`
"""


def calculate_square(number):
    # square number
    numberSq = number ** 2
    # return squared number
    return numberSq


def main():
    # user input
    number = int(input("Whats your lucky number? "))
    result = calculate_square(number)
    # print out `The square of <number> is <result>.`
    print(f"The square of {number} is {result}.")


main()



# Output:
# Whats your lucky number? 7
# The square of 7 is 49.

"""
---- No Return ----
def calculate_square():

    # Input & argument
    number = int(input("Whats your lucky number? "))
    result = number ** 2
    # Print out
    print(f"The square of {number} is {result}.")


# Calling Function
calculate_square()
"""
