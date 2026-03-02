# professor.py
# Andrew

'''
Ten Math Problems: The program should generate ten math problems. How might you implement this in your code?

Three Tries: The user should have up to three tries to answer each problem. If they answer incorrectly three times, the program
should display the correct answer. How might you implement this in your code?

Score: The program should keep track of the user’s score and display it at the end. How might you implement this in your code?
'''
import random

# Main Logic


def main():
    level = get_level()

    count = 0
    correctAnswers = 0

    while count < 10:
        errorCount = 0
        # Assigning x,y to randomize output
        x = generate_integer(level)
        y = generate_integer(level)

        count = count + 1

        # Expression
        answer = int(input(f"{x} + {y} = "))

        while (x + y) != answer:
            print("EEE")
            if errorCount < 3:
                if errorCount == 3:
                    errorCount += 1
                    print(f"{x} + {y} = {x + y}")
                    break
                answer = int(input(f"{x} + {y} = "))

            print(f"{x} + {y} = {x + y}")
            break

        correctAnswers += 1

    print(f"Score: {correctAnswers}")


def get_level():
    # Loop asking for level
    while True:
        try:
            # Asking for user to enter in level
            level = int(input("Level: "))
            #
            if 1 <= level <= 3:
                # Return level
                return level

        # Error Handling
        except ValueError:
            continue


def generate_integer(level):
    # Generate a integer based on level
    # Level 1 (0-9)
    if level == 1:
        rand_int = random.randint(0, 9)
        return rand_int

    # Level 2 (10-99)
    elif level == 2:
        rand_int = random.randint(10, 99)
        return rand_int

    # Level 3 (100-999)
    elif level == 3:
        rand_int = random.randint(100, 999)
        return rand_int


if __name__ == "__main__":
    main()
