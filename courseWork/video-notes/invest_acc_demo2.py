# Calculating Future investments
# Bruce / Andrew

def main():
    # print out intro message
    print("Welcome to the Future value calc. program")
    # ask for initail investment
    principal = eval(input("How much are you investing? "))
    # Intrest per year
    apr = eval(input("What interest percentage is being used?(Enter deciaml) "))
    # over 10 years
    for i in range(10):
        principal = principal * (1 + apr)
        print("The new principal is:", principal)
    # print out ending message
    print("The final principal affer 10 years is", principal)
    print("Program End")
main()
