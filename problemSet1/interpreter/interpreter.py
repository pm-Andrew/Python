# Math Interpreter interpreter.py
# Andrew


def main():
    # Asking for math expression
    expression = input("Enter math expression: ")
    # Splitting the expression
    x, y, z = expression.split(" ")

    if y == "+":
        print(float(x) + float(z))
    elif y == "-":
        print(float(x) - float(z))
    elif y == "*":
        print(float(x) * float(z))
    elif y == "/":
        print(float(x) / float(z))


main()



