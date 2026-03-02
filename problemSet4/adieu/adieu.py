# Adieu, Adieu
# Andrew


# m5-sb6.py

# import the inflect library
import inflect

# Create an inflect object
inflectEngine = inflect.engine()

# Create a variable to hold the list of friends
friends = []

# Infinite loop
while True:
    try:
        # Get a friend name from the user
        friend = input("Enter the name of a friend: ")
        # Append the friend to the friends list
        friends.append(friend)
    except EOFError:
        # User pressed control+d so lets end the while loop
        break

# Print out an extra line so output goes onto new line
print()
# Use the inflect join method to print out with , and to
print(f"Adieu, adieu, to {inflectEngine.join(friends)}")
