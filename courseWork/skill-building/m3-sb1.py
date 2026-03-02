# m3-sb1.python
# Andrew

"""
Write a Python program that uses a loop and a list containing the numbers [1,3,5,7,9,11,13,15,17,19,21]
to cube each of the numbers in the list. In a single print statement, print out the number being cubed
and the cubed value of that number. Place your code in a function named cubed(). Call the function to get
the program to execute.
"""

def cubed():
    for numbers in [1,3,5,7,9,11,13,15,17,19,21]:
        print(f"The number {numbers}, squares into {numbers ** 3}")


cubed()
