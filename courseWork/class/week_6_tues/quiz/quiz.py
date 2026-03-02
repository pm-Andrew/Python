# quiz.py
# Andrew
# Problem Set 3 ex.

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer. Please try again.")
    else:
        break
    finally:
        print("😯")

print(f"x is {x}")
