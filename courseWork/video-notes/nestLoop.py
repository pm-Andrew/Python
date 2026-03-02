# Nested Loops nestLoop.py
# Bruce / Andrew

def loopy():
    howMany = int(input("How many times should I loop? "))
    for i in range(howMany):
        for j in range(11):
            print(j, end=" ")
        print()

loopy()
