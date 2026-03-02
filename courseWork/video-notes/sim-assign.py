# Simultaneous Assignment sim-assign.py
#


a, b = eval(input("Enter two numbers: "))
print(a,b)

# # Input: 3,4
# # Output: 3 4

a,b,c = input("Enter three values: ").split()
print(a,b,c)

# # Input: 12, 42, Pizza
# # Output: 12 42 Pizza


a,b,c = input("Enter three values: ").split()
print(type(a),type(b),type(c))

# Input: 12, 42, Pizza
# Output: <class 'str'> <class 'str'> <class 'str'>


# We change the type of variable
a = int(a)
b = float(b)
print(type(a), type(b), type(c))
# Input: 12, 42, Pizza
# Output: <class 'int'> <class 'float'> <class 'str'>
