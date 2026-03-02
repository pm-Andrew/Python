# Meal Time meal.py
# Andrew S


"""
Breakfast: 7:00-8:00
Lunch: 12:00-13:00
Dinner: 18:00-19:00
"""


def main():
    # Asking for the time & and strip out ":"
    currTime = input("Whats time is it? ")
    # results converted
    result = convert(currTime)
    # The scope of convert
    if 7 <= result <= 8.5:
        print("Breakfast time")
    elif 12 <= result <= 13.5:
        print("Lunch time")
    elif 18 <= result <= 19.5:
        print("Dinner time")


# converting Time to a string
def convert(currTime):
    # Splitting ":" out
    hour, minute = currTime.split(":")
    hour = int(hour)
    minute = int(minute) / 60
    time = hour + minute
    return time

if __name__ == "__main__":
    main()
