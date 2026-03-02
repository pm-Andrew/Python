# Problem 3: Grocery List grocery.py
# Andrew


def main():
    # Empty dict for storage
    groceries = {}

    while True:
        try:
            # blank space for food items we are also returning in ALL CAPS
            food = input("").upper()
            # Check to see if item is in dict
            if food in groceries:
                groceries[food] = groceries[food] + 1
            else:  # Input not accepted
                # setting item qnty to 1
                groceries[food] = 1
        # Errors EOFError and KeyError
        except (EOFError, KeyError):
            # blank line for output readability
            print()
            # creating a list of groceries dict by set()
            foods = set(groceries)
            # sorting the list and returning new list
            foods = sorted(foods)
            # using the list to grab values from the groceries dict
            for food in foods:
                print(f"{groceries[food]} {food}")
            # Exit
            break


main()
