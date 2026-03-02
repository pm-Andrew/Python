# demo2.py
# Andrew

# Write code that ensures that a user enters a number from 1 to 10 (inclusivley)
# if they don't reprompt them to try again
# Once they give you a number between 1 and 10, thank them


while True:
    # get input form the user
    number = int(input("Enter a number between 1 and 10: "))

    # check to see if number is between 1 and 10
    if number >= 1 and number <= 10:
        print("Thanks for that number!")
        break

    # elif number >= 11 and number < 20:
    #     print("Try again - you are getting close!")

    # if you want to add an else you can
    # else:
    #     continue
# we can make this program simpler
