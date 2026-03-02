# Student Grade Calc m2-sb1.py
# Andrew 


# define main function
def main():
    # User number score
    score = int(input("Enter the score: "))
    # Establishing decisions
    if score == 5:
        grade = "A"
    elif score == 4:
        grade = "B"
    elif score == 3:
        grade = "C"
    elif score == 2:
        grade = "D"
    elif score == 1:
        grade = "F"
    elif score == 0:
        grade = "F"
    else:
        print ("*sigh*")


    # display converted grade
    print(f"The letter grade is {grade}")


# Run
main()




'''
---- V.1 ------
# User number grade
grade = int(input("Enter the score received: "))

# defining decisions in order
if grade == 5:
        print("You get an A")
elif grade == 4:
        print("You get a B")
elif grade == 3:
        print("You get a C")
elif grade == 2:
        print("You get a D")
elif grade == 1 or grade == 0:
        print("You get an F")
# if criteria isn't met display this
else:
        print("I can't give you a grade for that score")
'''
"""
----- ASK ----
- is this print vs return?
- Does order of variables matter? order of if, elif, else
"""
'''
----------- Solution ----------
# Module 2 Skill Building Exercise 1
# Author: Bruce Elgort


# define main function
def main():
    print("Quiz Grader\n")
    # get quiz score
    score = int(input("Enter the score (0-5): "))
    # use if's and elif's to determine what grade to assign
    if score < 2:
        grade = "F"
    elif score < 3:
        grade = "D"
    elif score < 4:
        grade = "C"
    elif score < 5:
        grade = "B"
    else:
        grade = "A"

    # display grade
    print(f"Grade is {grade}")


# start the program
main()
'''
