# Epic Gamer Energy Drinks
# Andrew

"""
A vending machine sells **Epic Gamer Energy Drinks** for 99cents
and only accepts coins in these dominations: 50 cents, 25 cents, 10 cents, and 5 cents.

Ex.

# if 5 in valid_coins:
#     print("You entered a valid coin")
# else:
#     print("Not a vaild coin")

"""

valid_coins = [5, 10, 25, 50]
amount = 0

# loop until we get at least 99 cents or more from the user
while amount < 99:
    print(f"Amount owed: {99 - amount}")
    # prompt payment
    payment = int(input("Insert a coin: "))
    # check to see if valid coin
    if 5 in valid_coins:
      # add the payment to the amount collected
      amount = amount + payment

# if we do get at least 99 cents or more we can dispense the energy drink
print("Enjoy your drink!")
# and then, we need to give them any change that they are owed
print(f"Change: {amount - 99}")


