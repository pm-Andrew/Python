# Guessing Game game.py
# Andrew

# Import
import random


def main():
    # Need a loop indefinite loop and at some point break out of the loop once game ends
    while True:
        try:
            # Ask for a level : n
            level = int(input("Level: "))
        # Catches invalid input
        except ValueError:
            continue
        # Check for + number. If not reprompt
        if level < 1:
            continue
        else:
            break

    # generate random 1 - n
    randomNumber = random.randint(1, level)
    while True:
        try:
            # User guess
            guess = int(input("Guess: "))
        except ValueError:
            continue
        # handling guess test if randomNumber is less than, greater than, or equal to the guess

        # too small
        if guess < randomNumber:
            print("Too small!")
            continue
            # too large
        elif guess > randomNumber:
            print("Too large!")
            continue
            # just right
        elif guess == randomNumber:
            print("Just right!")
        # break out of program
        break


# conditional program execution
if __name__ == "__main__":
    main()
