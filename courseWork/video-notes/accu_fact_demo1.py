# Factorial Example
# Bruce / Andrew

#

def main():
    num = eval(input("Enter a Number that you want to find the factorial of: "))
    fact = 1
    for factor in range(num, 1,-1):
        print("Current value of factor:", factor)
        fact = fact * factor
        print("Current value of fact:", fact, end= "\n\n")
    print("The factorial for", num, "is", fact)

main()
