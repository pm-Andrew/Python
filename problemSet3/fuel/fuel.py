# Fuel Gauge fuel.py
# Andrew

def main():
    while True:
        # get a fraction from the user
        fraction = input("Enter a fraction: ")
        # we don't want a fraction that does not contain number (1/4)
        if "/" in fraction:  # if there is "/"
            x, y = fraction.split("/")
            try:  # try and convert x & y to int
                x = int(x)
                y = int(y)

                # if y = 0
                if y == 0:
                    continue

                # if x is greater than y
                if x > y:
                    continue

                # Calculate fraction to percentage
                percentage = round(x/y * 100)

                # Empty
                if percentage <= 1:
                    print("E")
                # Full
                elif percentage >= 99:
                    print("F")
                else:
                    # Print out percentage
                    print(f"{percentage}%")

                # Get out of while loop
                break
            # pass the program if these errors pop-up
            except (ValueError, ZeroDivisionError):
                pass


main()
