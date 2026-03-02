# mario.py
# Andrew

def build(number):
    for i in range(number):
        print("#" * (i + 1))
# Alt. way of interating
    # for i in range(1, number, +1):
    #    print("#"* i)


def main():
        howMany = int(input("How large of a ladder would you like? "))
        build(howMany)



main()
