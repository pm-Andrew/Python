# Conditionals.py
# Carter Zenke Youtube video


def main():
	# User input
	difficulty = input("Difficult or Casual ")
	players = input("Multiplayer or Single-player? ")
	# players & difficulty are variables with inputs being stored
	# 'if' is the keyword to make this a conditional
	# 'if' is then followed by a boolean expression
	if difficulty == "Difficult":
	# we can narrow down the recommendation
		if players == "Multipler":
			recommend("Poker")
		elif players == "Single-player":
			recommend("Klondike")
		# if the condition is not true
		else:
			print("Enter a vaild numer of players")
	elif difficulty == "Casual":
		if players == "Multiplayer":
			recommend("Hearts")
		elif players == "Single-player":
			recommend("Clock")
		else:
			print("Enter a valid difficulty")

def recommend(game):
	print("You must like", game)


main()
