# cards
# Andrew

# import random

# cards = ["jack", "queen", "king"]

# def main():
#     print(random.choice(cards))

# main()


import random

cards = ["jack", "queen", "king"]

def main():
    # seed goes into a pseudorandom number generator
    # gives a random key that stays consistant
    random.seed(0)
    # k= number of item i want to choice
    print(random.choices(cards, k=2))


main()
