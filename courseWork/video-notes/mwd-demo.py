# Multi-Way Decisions mwd-demo.py
# Bruce Elgort /Andrew


grade = int(input("Enter the score received: "))

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
else:
        print("I can't give you a grade for that score")
