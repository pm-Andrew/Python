# problem4.py
# Calculate Area of Circle


"""
Write a function called `circle_area` that:
1. Takes one argument: `radius`.
2. Returns the area of a circle, using the formula:
   `Area = π * radius^2`
   Use `3.14` as the value of π.

Ask the user for the radius of the circle, call the function, and print the result as:
`The area of the circle is: <area>.`
"""


def circle_area(radius):
    # calculate area of circle
    area = 3.14 * radius ** 2
    # end function and return expression value
    return area


def main():
    # ask for user input
    radius = float(input("Radius to Area convert! Radius: "))
    # call back function
    result = circle_area(radius)
    # print results
    print("The area of the circle is:", result)


main()



# Output:
# Radius to Area convert! Radius: 6
# The area of the circle is: 113.04



'''
----- No Return -----
# function
def circle_area():

    # input
    radius = float(input("Give me a number 1-9 "))
    # doing the math
    area = 3.14 * radius ** 2

    # print
    print("The area of the circle is: area.")


# Calling Function
circle_area()
'''
