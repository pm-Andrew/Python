# m4-sb7.py
# Andrew


def main():
    inventory = {}  # Create an empty dictionary

    print("Welcome to the inventory program!")
    print("Press control+d to stop adding items to the inventory.")

    while True:
        try:
            item = input("Enter an item: ")  # Get user input

            # If the item is in the inventory increase quantity by 1
            if item in inventory:
                # Get current number and add one to it
                inventory[item] = inventory[item] + 1
            else:  # Item is not in the dictionary
                # Add the item to the dictionary and set quantity to 1
                inventory[item] = 1
        except EOFError:  # Trap that control+d was pressed
            # Print out a blank line
            print()
            # Lets first sort the dictionary
            # Step 1 - This will create a list of the items in the dictionary
            items = set(inventory)
            # Step 2 - Sort the list
            items = sorted(items)
            # Step 3 - Use the items list to get the values from the dictionary
            for item in items:
                print(f"{item} Quantity {inventory[item]}")
            # Break out of the loop
            break


main()
