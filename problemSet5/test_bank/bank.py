# Bank 2.0 bank.py
# Andrew


def main():
    # asks for input then strips whitespace and converts to lowercase
    greeting = input("Greeting: ").strip().lower()
    # setting greeting to greeting()
    greeting = value(greeting)
    # print out the returned values
    print(f"${greeting}")


def value(greeting):

    # running an if-else to check
    if greeting.startswith("hello"):
        # return 0 as an int
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
