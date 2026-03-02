# problem7.py
# Favorite Color Function


"""
Write a function called `favorite_color` that:
1. Takes one argument: `color`.
2. Returns a string like:
`Wow, <color> is an awesome color!`

Ask the user for their favorite color, call the function, and print the result.
"""

# defining function


def favorite_color(color):
    # return `Wow, <color> is an awesome color!`
    return f"Wow, {color} is an awesome color!"


def main():
    # ask user for their favorite color
    color = input("What is your favorite color? ")
    # call favorite color function
    result = favorite_color(color)
    print(result)


main()


# Output:
# What is your favorite color? Green
# Wow, Green is an awesome color!
