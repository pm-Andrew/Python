# 48 Laws of Power project.py
# Andrew

# to read 48_laws.csv
import csv
# to help with logic
import sys
# import random library
import random


# welcome message
print("Welcome!\nThis program Summarizes The 48 Laws of Power\n------")


def main():
    # Open dict to store list of dicts
    all_laws = []

    # 1st building the list with the dicts
    # for debugging ("./final-project/48_laws.csv")
    with open("48_laws.csv") as file:
        # use DictReader to read dicts
        reader = csv.DictReader(file)
        # for each row, read.
        for row in reader:
            # append as a list with dict inside
            all_laws.append({
                "number": row["number"],  # number is the law number
                "law": str(row["law"]),  # law is the law decription
                "summary": str(row["summary"]),  # summary is the law summary
                "figure": str(row["figure"])  # figure is figure involved with the law
            })

    # Asking the user for a number that is 1-48 loop
    while True:
        try:
            # Input needs to be an int for if loop below
            user_law = input("What Law would you like to learn? ").strip()

            # If Empty input
            if user_law == "":
                # get a random law
                law = random_law(all_laws)
                # right out random law
                sys.exit(law)

            # assigning law to is_law with 2 arguments user_law and all_laws dict
            law = is_law(user_law, all_laws)

            # if from is_law returns False
            if law == False:

                # reprompt
                continue
            # if True
            else:
                print(f"""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Law: {law['law']}
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)
                break

        # Error handling
        except ValueError:
            #  Error
            break

    # if valid law is entered
    if law:
        # After law is picked ask what info
        figSum = input(
            "\nWould you like to a short summary or a historical figure? (summary or figure): ").lower()

        # calling lawFork into main
        results = lawFork(figSum, law)
        # print either summary, figure, or both
        print(results)


def is_law(user_law, all_laws):
    # iterating through a list of dicts from main()
    for row in all_laws:
        # print entered law value entered my user
        if user_law in row["number"]:
            # return value to main
            return row
    # continue
    else:
        return False


# checking to see if user wants to know more about the law
# if they press enter exit program
def lawFork(figSum, law):
    # decision fork
    # User entered 'sum' or 'summary'
    if figSum == "sum" or figSum == "summary":
        return f"""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Summary: {law['summary']}
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
     # User entered 'fig' or 'figure'
    elif figSum == "fig" or figSum == "figure":
        return f"""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Figure: {law['figure']}
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
     # User entered 'sum and fig' or 'both'
    elif figSum == "both" or figSum == "sum and fig":
        return f"""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        Summary: {law['summary']}
        Figure: {law['figure']}
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
    # Error message
    else:

        return f"""
        ~~~~~~Hints~~~~~~~
        |- summary OR sum |
        |- figure OR fig |
        |- sum and fig OR both |
        ~~~~~~~~~~~~~~~~~~~~~
        """


def random_law(all_laws):
    # When user presses enter, for input they get a random law
    # {'number': '22', 'law': '22. Use the Surrender Tactic: Transform Weakness into Power', 'summary': 'Yielding can be a strategic move.', 'figure': 'Napoleon Bonaparte'}
    # 'law: "law", summary: "summary", figure: "figure"
    law = random.choice(all_laws)
    # return random law in `law` to send up to the main
    return law


if __name__ == "__main__":
    main()
