# camelCase
# Andrew


def main():
    # Asking for input in camelCase
    c_case = input("camelCase: ")
    s_case = convert(c_case)
    print("snake_case:", s_case)


# If camelCase convert to snake_case
def convert(c_case):
    s_case = ""
    for char in c_case:
        # Finding upperCase and adding '_' whiile lowering the case
        if char.isupper():
            s_case += "_" + char.lower()
        else:
            s_case += char
    # Returning converted string
    return s_case


main()
