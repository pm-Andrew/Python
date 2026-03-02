def main():
    print("Five point quiz grader")
    # ask for user input
    score = eval(input("Enter the score: "))
    # locate position within the string
    grade = FFDCBA[score]
    # display result
    print(f"The grade is {grade}")


main()
