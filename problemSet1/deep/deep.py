# Deep Though deep.py
# Andrew


"""
# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life,
# the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two
# or forty two. Otherwise output No.
"""


def main():
    # calls ask_question with question returned
    question = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    # calling check_answer with an argument
    check_answer(question)
    


# 42? - Yes| Forty Two - Yes | Forty-Two - Yes | if not... NO
def check_answer(question):
    if question == "42" or question == "forty two" or question == "forty-two":
        print("Yes")
    else:
        print("No")

main()

