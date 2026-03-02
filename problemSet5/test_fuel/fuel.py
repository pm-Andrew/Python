# fuel.py
# Andrew


def main():
    while True:
        fraction = input("Fraction: ")
        percentage = convert(fraction)
        print(gauge(percentage))
        break


def convert(fraction):
    # Catch str in input 'cat/dog'
    try:
        # split into numerator & denominator
        x, y = fraction.split("/")
        # change x & y to integers
        x = int(x)
        y = int(y)

        # check to see if x is between 0 and 100
        # 1 and 10 are the ranges
        if x < 0 or x > 100:
            raise ValueError

        # check to see if y is between 0 and 100
        # 1 and 10 are the ranges
        if y < 0 or y > 100:
            raise ValueError

        # Checking for undefined fraction to raise a ZeroDivisionError
        if y == 0:
            raise ZeroDivisionError

        if x > y:
            raise ValueError

        return round(x/y * 100)

    except ValueError:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"

    if percentage >= 99:
        return "F"

    return f"{percentage}%"


if __name__ == "__main__":
    main()
