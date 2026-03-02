# problem5.py
# Simple Calculator


"""
Write a function called `add_numbers` that:
1. Takes two arguments: `num1` and `num2`.
2. Returns the sum of the two numbers.

Ask the user for two numbers, call the function, and print the result as:
`The sum of <num1> and <num2> is <result>.`
"""

# function


def add_numbers(num1, num2):
    theSum = num1 + num2
    return theSum


def main():
    # input
    num1 = int(input("Give me a number: "))
    num2 = int(input("Give me another number: "))
    # Math-magical mathing
    result = add_numbers(num1, num2)

    # print
    print(f"The sum of {num1} and {num2} is {result}.")


# calling the function
main()


# Output:
# Give me a number: 56
# Give me another number: 2
# The sum of 56 and 2 is 58.
