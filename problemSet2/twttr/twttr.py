# twttr.py
# Andrew


def main():
    # Ask for input
    word_one = input("Input: ")
    word_two = convert(word_one)
    print("Output:", word_two)


# here we will iterate through strings and removing the vowels a, e, i, o, & u
def convert(word_one):
    word_two = ""
    for char in word_one:  # finding vowels upper and lower
        if char in "aeiouAEIOU":
            pass  # nothing done after found and removed
        else:
            word_two += char  # removing vowels
    # returning converted string
    return word_two


main()
