# While Loop demo2 whileLoop_demo.py
# Bruce / Andrew

def main():
    for i in range(5):
        print(i,"do something")

def whileDemo():
    # While loop
    # Set initial calue to 0
    condition = 0
    # keep looping while condition > 0
    while(condition >= 0):
        print("I'm in a while loop")
        # whats the new value
        condition = eval(input("Ask for value of conditions: "))

whileDemo()
