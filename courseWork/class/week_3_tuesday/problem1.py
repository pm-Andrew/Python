# problem1.py
# Greeting Function


"""
Write a function called `greet` that:
1. Takes one argument: `name`.
2. Prints a personalized greeting like:
`Hello, <name>! Welcome to Python.`

Then, call the function and pass it a name provided by the user.

Example:
Enter your name: Bruce
Output: Hello, Bruce! Welcome to Python.
"""

# Define Function
def greet():
# input
    name = input('Hello, what is your name! ')
    print(f'Hello, {name}! Welcome to Python')

greet()


# Output:
# Hello, what is your name! Andrew
# Hello, Andrew! Welcome to Python
