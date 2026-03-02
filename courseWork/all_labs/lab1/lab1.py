# lab1.py
# Andrew


# constants
LOCALTAXRATE = .10
MEDICALRATE = .12

# get input
name = input("Enter name: ")
hourlyWage = float(input("Enter hourly wage: "))
hoursWorked = float(input("Enter the number of hours worked during the week: "))

# Perform Calculations

if hoursWorked > 40:
    wages = 40 * hourlyWage
    overtimeWages = (hoursWorked - 40) * (hourlyWage * 1.5)
else:
    wages = hoursWorked * hourlyWage
    overtimeWages = 0

# net pay calculations
totalWages = wages + overtimeWages
taxes = totalWages * LOCALTAXRATE
medical = totalWages * MEDICALRATE
netPay = totalWages - taxes - medical

# Print out
print()
print(f"Name: {name}")
print(f"Hourly wage: ${hourlyWage:.2f}")
print(f"Local taxes: ${taxes:.2f}")
print(f"Medical insurance: ${medical:.2f}")
print(f"Overtime pay: ${overtimeWages:.2f}")
print(f"Total gross earnings: ${totalWages:.2f}")
print(f"Net pay: ${netPay:.2f}")
