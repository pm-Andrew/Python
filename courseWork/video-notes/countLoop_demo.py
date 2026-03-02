# countLoop_demo.py
# Andrew

# below are 4 examples of performing a counted loop using the rang() function
# this is a "counted loop" that will execute 10 times

for i in range(10): # starts the count at 0-9
    print("The zvalue of the loop iterator 'i' is:", i)
# range() creates a list to interate through


# this is the same as above using a different variable for the iterator

for number in range(10):
    print("The value of the loop iteator 'number' is:", number)


# here is a count that iterates from 0 to 10 stepping up by 2 during each iteration
# notice how there are now 3 parameters in the range() function

for counter in range(0,12,2): # The position of 12 is count limit but skip then count by 2
    print("The Value of 'counter' is:", counter)

# outside of canvas

for number in range(5):
    theNumber = int(input("Enter an integer: "))


