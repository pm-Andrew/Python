#demo5.py
#Andrew

# DRY - Don't Repeat Yourself

def add_two_numbers():
    # Get number from Human
    number1 = float(input("Enter a number: "))
    # Get another from a Human
    number2 = float(input("Enter a number: "))
    # calculate the sum
    number_sum = number1 + number2
    # Print out the Sum
    print(f"The sum of {number1} + {number2} = {number_sum}")
# : at the end of a statment, means the code below gets indented, def is creating your own function
# def is reusable code
# watch out for if variables are greyed out, that is signaling that you need to use the variable in the code
add_two_numbers()

