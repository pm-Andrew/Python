# Accumulator Pattern demo3
# Andrew

# adding up 5 numbers entered by a person

total = 0

for i in range(5):
    aNumber = float(input("Please enter a number: "))
    total = total + aNumber

print("The total of the 5 numbers is", total)
