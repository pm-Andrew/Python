# problem10.py
# Fix the Function (Debugging Challenge)

# The following function is supposed to calculate the total cost after tax but has errors. Fix it:

def total_cost(price, tax_rate):
    total = price + price * tax_rate
    return total

price = float(input("Enter the price: "))
tax = float(input("Enter the tax rate: "))
print(f"The total cost is: {total_cost(price, tax):.2f}")


# Output:
# Enter the price: 2.99
# Enter the tax rate: .03
# The total cost is: 3.08
