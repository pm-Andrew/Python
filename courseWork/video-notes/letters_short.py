# letters_short.py
# Andrew


def main():
    # this gives a dictionary that enables a for loop 0-3
    names = ["Mario", "Lugi", "Dasiy", "Yoshi"]
    # i = name
    for name in names:
        print(write_letter(name, "Princess Peach"))


# Our letter with reciver and sneder as the arguements
def write_letter(reciver, sender):
    return f"""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Dear {reciver},

        You are cordially invited to a call at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {sender}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

main()
