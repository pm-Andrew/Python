# twttr.py
# Andrew


def main():
    # Ask for input
    word = input("Input: ")
    word_two = shorten(word)
    print("Output:", word_two)


# here we will iterate through strings and removing the vowels a, e, i, o, & u
def shorten(word):
    word_two = ""
    for char in word:  # finding vowels upper and lower
        if char in "aeiouAEIOU":
            pass  # nothing done after found and removed
        else:
            word_two += char  # removing vowels
    # returning converted string
    return word_two

if __name__ == "__main__":
    main()
