# Boolean Expressions booExpress.py
# Carter Zenke Youtube video

def main(): # this has a boolean response, and then we can use boolean operators () should be evaluationed first
	difficulty = input("Difficult or Casual? ")
	if not (difficulty == "Difficult" or difficulty == "Casual"):
		print("Enter a valid difficulty")
		return # end of the program


	players = input("Multiplayer or Single-player? ")
	if not (players == "Multiplayer" or players == "Single-player"):
		print("Enter a valid number of players")
		return # end of the program
# We've now seen here how we can use these logical expressions-- and actually,
# Boolean expressions and Boolean operators--to combine these together and ask more complex questions about user input.

	if difficulty == "Difficult" and players == "Multiplayer":
		recommend("Poker")
	elif difficulty == "Difficult" and players == "Single-player":
		recommend("Klondike")
	elif difficulty == "Casual" and players == "Multiplayer":
		recommend("Hearts")
	else:
		recommend("Clock")


def recommend(game):
	print("You must like", game)

main()


