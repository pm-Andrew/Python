# Try and Except try.py

def main():
    x = 20
    y = 0
    try: # if something happens follow below
        z = x/y
    except ZeroDivisionError:
        print("You can not divide a number by 0")

    try:
        print(a) 
    except NameError:
        print("Variable not defined")

    try:
        math.sqrt(9)
    except: # generic exception
        print("Something went wrong")

main()
