# m5-sb4.py

import random

# Function to get a number from user. The prompt paremter allows you to pass in a string that the input will use
def getNumber(prompt):
    # Forever/Infinite loop
    while True:
        # get input using the prompt supplied
        number = input(prompt)
        # check to make sure it's a number
        if number.isdigit():
            # return the number entered
            return number


# Main logic for program
def main():
    # Call getNumber function with prompt
    level = int(getNumber("Level: "))

    # Generate random number between 1 and level
    randomNumber = random.randint(1, level)

    # Print result
    print(f"The random number generated was {randomNumber}")


# Invoke the program
main()
