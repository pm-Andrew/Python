# Problem 2: Felipe's Taqueria taqueria.py
# Andrew


def main():
    # Menu Dict item: cost
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # open variable that we change below
    total = 0

    while True:
        try:
            # Getting user order
            order = input("Item: ").title()
            # call item from menu dict
            if order in menu:
                # Adding items together
                total = total + menu[order]
            # IF not in menu dict, loop
            else:
                continue
        # ctrl + d error
        except EOFError:
            # Ends Loop once error is triggered
            break
        # prints out total cost of order
        print(f"Total: ${total:.2f}")


main()
