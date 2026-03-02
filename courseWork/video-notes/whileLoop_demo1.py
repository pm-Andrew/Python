# While Loops demo whileLoop_demo.py
# Bruce / Andrew

def main():
    answer = True
    while(answer):
        # ident to give parameters to the loop
        answer = input("Enter something. Simply press enter to quit ")
        # here is setting 'enter' to escape program
        if answer == ' ':
            answer == False

main()
