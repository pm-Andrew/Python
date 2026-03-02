# duck.py
# Andrew

# # Count down form 100 to 0
# # range([start,]stop,[step]) default values of [step] is 1
# for i in range(100, -1, -3):
#     print(i)

a = int(input("Enter starting Number: "))
b = int(input("Enter endig Number: "))
c = int(input("Enter Number to step: "))


for i in range(a,b,c):
    print(i)
