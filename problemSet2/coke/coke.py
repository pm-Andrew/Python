# Coke Machine coke.py
# Andrew


due = 50
amount = 0

#
while amount < 50:
    print("Amount Due:", due - amount)
    coin = int(input("Insert Coin: "))
    # check to see if coins are 5, 10, 25
    if coin == 5 or coin == 10 or coin == 25:
        amount = amount + coin

if amount >= due and coin:
    change = amount - due
    print(f"Change Owed: {change}")
'''

Suppose a machine sells bottles of Coca-Cola (Coke) for 50 cents and
only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents

Once the user has inputted at least 50 cents, output how many cents in change,
the user is owed. Assume that the user will only input integers, and ignore any
integer that isn’t an accepted denomination.

'''
