# Nutrition Facts nutrition.py
# Andrew

# providing a dictionary with fruit: calories
fruit = {
    "apple": 130,
    "avocado":  50,
    "banana": 100,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon":  50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime":  20,
    "nectarine":  60,
    "orange":  80,
    "peach":  60,
    "pear": 100,
    "pineapple":  50,
    "plums":  70,
    "strawberries":  50,
    "sweet cherries":  100,
    "tangerine":  50,
    "watermelon":  80
}
# asking for input
calories = input("Item: ").lower()
while calories in fruit:
    print("Looping")
    # if True continue to print calories
    # if calories in fruit:
        # prints out calories of fruit
    print("Calories:", fruit[calories])
    break
