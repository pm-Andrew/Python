# problem6.py
# Fix the Function (Debugging Challenge)


# The following code is supposed to calculate the cube of a number,  #but it contains errors. Fix it so it works as expected:

def calculate_cube(number):
    return number ** 3


def main():
    num = int(input("Enter a number: "))
    result = calculate_cube(num)
    # print
    print(f"The cube of + {num} + is  + {result}")

main()


# Output:
# Enter a number: 9
# The cube of + 9 + is  + 729
