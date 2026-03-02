# CTEC 121 - Winter 2025
# Final Exam / Project

import random


def roll_dice(num_rolls=1):
    """Rolls a six-sided die num_rolls times and returns the highest value."""

    """
    How it Works:
    - The function takes one parameter, num_rolls, which determines how many times the die is rolled.
	- It generates a random number between 1 and 6 for each roll.
	- It keeps track of the highest number rolled and returns it.

    Why?
	- This makes the game more interesting because rolling multiple times gives the player a better chance at a high number.
	- Used in battles and decision-making to introduce an element of luck.

    Hints:
	- Use the random.randint(1, 6) function to simulate rolling a six-sided die.
	- If num_rolls is greater than 1, roll the die multiple times and return the highest value.
    - So if the funciton is called with roll_dice(3) you are to roll the dice 3 times and return the highest value.
	- Consider using a for loop and a variable to track the highest number rolled.
    - Use the Duck Debugger as necessary.
    """

    # TODO: Implement rolling a die multiple times and returning the highest value
    pass


def find_treasure():
    """Randomly selects a treasure with possible game effects."""

    """
    How it works:
	- A dictionary stores different treasures and their effects.
	- The function randomly selects one treasure using random.choice().
	- It returns a tuple containing the treasure name and its effect.

    Why?
	- The treasure might help the player (e.g., a magic potion for battle) or just be for fun.
	- Adds randomness and excitement to the game.

    Hints:
	- Create a dictionary where the keys are treasure names (e.g., "gold coins", "a magic potion", "an ancient key", "a shiny gem") and the values describe their effects.
	- Use random.choice() to pick a treasure at random.
	- Return both the treasure name and its effect as a tuple.
    - Use the Duck Debugger as necessary.
    """

    # TODO: Define a dictionary of treasures and their effects
    # TODO: Randomly select a treasure from the dictionary
    pass


def battle_monster(player_attack, monster_strength, has_potion):
    """Determines if the player wins a battle against a monster."""

    """
    This function determines if the player wins or loses a battle against a monster. The function should return True if the player wins and False if they lose.

    Example 1: Player wins without a potion

    battle_monster(6, 4, False)

    - The player attack is 6, the monster strength is 4.
	- The player wins because 6 > 4.
	- Return value: True

    Example 2: Player loses without a potion

    battle_monster(3, 5, False)

    - The player attack is 3, the monster strength is 5.
	- The player loses because 3 < 5.
	- Return value: False

    Example 3: Player has a potion and wins

    battle_monster(4, 6, True)

    - The player attack is 4, the monster strength is 6.
	- The player has a potion, which should increase their attack power.
	- If the potion adds, for example, +3 attack power, the new attack power becomes 4 + 3 = 7.
	- The player now wins because 7 > 6.
	- Return value: True

    Hint:
	- Compare player_attack and monster_strength to determine the battle outcome.
	- If has_potion is True, increase player_attack before comparison.
	- Return True if the player wins (player_attack > monster_strength), otherwise return False.
    """

    # TODO: If the player has a potion, increase their attack power
    # TODO: Compare player_attack to monster_strength and return True or False
    pass


def solve_puzzle():
    """Presents a random puzzle for the player to solve."""

    """
    How it works:
	- A dictionary stores puzzle questions as keys and their correct answers as values.
	- The function randomly selects one puzzle using random.choice().
	- It returns a tuple containing the puzzle question and the correct answer.

    Why?
	- Adds a thinking challenge to the game instead of relying only on luck.
	- Players must correctly answer the puzzle to continue their journey.

    Hint:
	- Create a dictionary with simple puzzles as keys and their correct answers as values.
    - Use the list() function to make the dictionary into a list
	- Use random.choice() to select a random puzzle.
	- Return both the puzzle question and the correct answer. Positions 0 and 1 from the random choice.

    Example puzzles to include:
	- "What is 5 + 3?" -> 8
	- "What color is the sky?" -> "blue"
	- "What is 10 divided by 2?" -> 5
    """

    # TODO: Create a dictionary with questions as keys and answers as values
    # TODO: Randomly select one puzzle and return the question and answer
    pass


def choose_door(choice, has_key):
    """Determines if the player successfully escapes the dungeon."""

    """
    How it works:
	- If the player has a key, they automatically succeed in escaping.

	- If the player does not have a key, the function randomly decides if the chosen door leads to freedom.
	- Only doors 1 and 2 are valid choices; any other choice results in failure.

    Why?
	- Introduces an element of risk and chance if the player lacks a key.
	- Rewards players for finding the ancient key earlier in the game.

    Hint:
	- If has_key is True, the player automatically wins.
	- If has_key is False, randomly determine whether the player succeeds or fails.
	- Use random.choice([True, False]) or random.randint(1, 6) to introduce chance-based outcomes.
    """

    # TODO: If the player has a key, they automatically succeed
    if has_key == True:
        ...
    elif has_key

    # TODO: If the player doesn't have a key, roll a die to determine success
    pass


def main():
    print()
    print("Welcome to 'Escape the Dungeon'!")
    print()
    input("Press Enter to roll the dice and begin...")

    # Roll dice
    dice_result = roll_dice()

    print()
    print(f"You rolled a {dice_result}!")
    print()

    # Find a treasure
    print("You found a treasure chest!")
    print()

    treasure, effect = find_treasure()

    print(f"Inside, you find {treasure}! {effect}")
    print()

    # Properly define has_potion and has_key
    has_potion = False
    has_key = False

    if treasure == "a magic potion":
        has_potion = True
    else:
        has_potion = False

    # Battle a monster
    print("A monster blocks your path!")
    print()

    player_attack = roll_dice()
    monster_strength = roll_dice()

    print(f"You attack with power {player_attack}, monster has {monster_strength} strength.")
    print()

    if battle_monster(player_attack, monster_strength, has_potion):
        print("You defeated the monster!")
    else:
        print("The monster overpowers you. You barely escape!")

    # Solve a puzzle
    print()
    print("A puzzle blocks your way. Solve it to continue!")
    print()

    puzzle, correct_answer = solve_puzzle()
    player_answer = input(f"{puzzle} ").strip().lower()

    if player_answer == correct_answer.lower():
        print()
        print("Correct! You may proceed.")
    else:
        print()
        print("Wrong answer! A trap door opens, but you escape just in time.")

    # Choose a door
    print()
    print("Two doors stand before you. One leads to freedom, the other to danger.")
    print()

    try:
        player_choice = int(input("Choose door 1 or 2: "))
        if choose_door(player_choice, has_key):
            print()
            print("You chose wisely and escape the dungeon!")
        else:
            print()
            print("The door won't budge! But after searching, you find another way out.")
    except ValueError:
        print()
        print("Invalid input! The door won't budge, but you find another way out eventually.")

    print()
    print("Congratulations! You've completed the game.")
    print()


if __name__ == "__main__":
    main()
