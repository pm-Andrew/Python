# Emojize.py
# Andrew


# import the emoji library
import emoji


def main():
    # Asking a user for a input of emoji in english
    phrase = input("Input: ")

    # print out the emojize str and deals with alias
    print("Output:", emoji.emojize((phrase), language='alias'))


main()
