# problem8.py
# Double a Number


"""
Write a function called `double_number` that:
1. Takes one argument: `number`.
2. Returns twice the value of the number.

Ask the user for a number, call the function, and print the result as:
`Double of <number> is <result>.`
"""


# Function called 'double_number' and adding an argument
def double_number(number):
    # return twice the value
    return number * 2


def main():
    # asking for input
    number = int(input("Provide a Number: "))
    # defining the result with function above
    result = double_number(number)
    # Print result
    print(f"Double of {number} is {result}")

# start program
main()


# Output:
# Provide a Number 3
# Double of 3 is 6
