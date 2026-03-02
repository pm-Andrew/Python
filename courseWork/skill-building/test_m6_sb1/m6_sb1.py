# Module 6 Skill-Building Exercise 1
# Andrew

"""
In the test_m6_sb1 folder, write a Python file named, m6_sb1.py a program that does the following:

- Uses the main() function to get input from the user and have them enter a sentence.
- Within the main() function, call a function named shorten, that passes into it the sentence entered by the user.
- Create the shorten function and have it receive the sentence entered in the main function.
- Write code to replace any spaces in the sentence with "". That's right, remove any spaces.
- Return the sentence back to the main function, where it gets printed out.
- Test your code to ensure it works by running python m6_sb1.py from the terminal command line.
"""


def main():
    # get input stripping whitespace
    sentence = input("Sentence: ").strip()
    # passing shorten through sentence
    sentence = shorten(sentence)
    print(f"Output: {sentence}")

# create shorten and pass sentence


def shorten(text):
    # sentence now text replaces whitespace with ","
    text = text.replace(" ","")
    # returning sentence
    return text


if __name__ == "__main__":
    main()
