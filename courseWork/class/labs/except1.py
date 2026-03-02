# Execpt1.py
# Andrew


while True: # will only stop if True
    try: # We are hoping for a number
        number = int(input("Enter a number: "))
    # We want only numbers
    except ValueError:
        print("I needed an integer number, not what you entered.")
    except ZeroDivisionError:
        print("A zero division error has occurred")
        break
    else:
        print("You entered the number", number)
        break
