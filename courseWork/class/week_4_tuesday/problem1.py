# problem1.py
# Your Name

"""
Nap Time Calculator

Problem:
Implement a program that prompts the user for the current
time in 24-hour format (#:## or ##:##) and a desired nap
duration in minutes. The program should calculate and output
the time the user should wake up after the nap.

For example:
- Input: 13:45 and 90
- Output: 15:15
- Input-2: 7:12 and 33
- Output-2: 7:45
"""
'''
# With this program we want to take a str to an interger
time = "13:45"
print(time.split(":"))

#Output: ['13', '45']
# this is a list
'''
# time = "13:45" # hardcode
# nap_time = int("90")
time = input("Enter a time: ")
nap_time = int(input("How long will your nap be: "))
hour, minute = time.split(":")
# this program here is outputting string values
# Lets define variables wrapped in int()
hour = int(hour)
minute = int(minute)

# mutliply the hour by 60. gives minutes.
total_minutes = hour * 60
# add minute to total_minutes
total_minutes = total_minutes + minute
# add the nap_time to the total_minutes
total_minutes = total_minutes + nap_time
# print out total_minutes
# print(total_minutes)
# divide total_minutes by 60
converted_time = total_minutes / 60
# 15.25 which is a float
# how do we get the 15?
hour, minute = str(converted_time).split(".")
# Now prints out the hours and minutes splitted as strings
# 15:15 is the goal output
# minute = int((int(minute) / 100)) * 60
minute = int(round((converted_time - int(hour))*60))
minute =str(minute).zfill(2)
# print(minute)
print(f"{hour}:{minute}")


# THis program is way to complicated
