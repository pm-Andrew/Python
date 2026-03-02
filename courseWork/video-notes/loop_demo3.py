# demo3.py
# Andrew


def get_number(num1, num2, prompt):

    # create an infinite loop or a forever loop
    while True:
        number = float(input(prompt))
        # check the number
        if number >= num1 and number <= num2:
            # send value of number back
            return number


def main():
    # get a number between 23 and 42 and prompt them for these numbers as ages
    print(get_number(23, 42, "Please enter an age between 23 and 42: "))
    # get a number between 0 and 4 and prompt for a gpa number between 0 and 4
    print(get_number(0, 4, "Please enter a GPA: "))
    # get a number between .3 and .9 and prompt them for the readings from a machine in the auto shop
    print(get_number(.3, .9, "Please enter am reading from shop machine between : "))



# call the main
main()
