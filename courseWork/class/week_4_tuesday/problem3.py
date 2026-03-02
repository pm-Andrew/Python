# problem3.py
# Your Name

"""
Write a program that calculates how much each
person needs to pay for a shared bill.
Prompt the user for the total bill amount, the
number of people, and the tip percentage in the
format amount people tip%. Then, calculate and
output the amount each person owes.

For example:
- Input: 100 4 15
- Output: Each person owes: $28.75
"""


def converter(data):
    # this is simultaneous assignment / bust apart the data
    cost, number_of_people, tip = data.split(" ")
    # convert all strings to numbers
    cost = float(cost)
    number_of_people = int(number_of_people)
    tip = float(tip)

    amount_of_tip = cost * (tip / 100)
    cost_of_meal_with_tip = amount_of_tip + cost
    cost_per_person = cost_of_meal_with_tip / number_of_people

    return cost_per_person


def main():
    # this is a string
    data = input("Enter the cost, number of people, and the tip percentage: ")
    result = converter(data)
    # how to we calculate how much each person owes
    print(f"The amount each person is ${result:.2f}")


main()
