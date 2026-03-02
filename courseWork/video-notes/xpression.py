# 1 + 1

expression = input("Enter math expression: ")

num1,operator, num2 = expression.split(" ")

# print(type(expression))
# print(num1, num2, operator)

if operator == "+":
        print(int(num1)+ int(num2))
