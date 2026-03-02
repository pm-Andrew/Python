# Class - Methods and Variables

class Food:
    # creating a clss variable
    base_hearts = 1

    def __init__(self, ingredients):
        # instance variables
        # ingredients
        self.ingredients = ingredients
        # hearts - calling classmethod calculate_hearts() with ingredients as input
        self.hearts = Food.calculate_hearts(ingredients)

    # decorator for classmethod
    @classmethod
    # cls is short for typing Food? cls == self.
    def calculate_hearts(cls, ingredients):
        # starting with food being 1 heart
        hearts = cls.base_hearts

        # for loop to add value to each ingredient
        for ingredient in ingredients:
            # "Hearty" keyword double/ 2
            if "hearty" in ingredient.lower():
                # increase by 2
                hearts += 2
            else:
                # increase by 1
                hearts += 1
        # return heart vaule
        return hearts

    @classmethod
    # new food item from no ingredients
    def from_nothing(cls, hearts):
        # food is a new instance of Food w/ empty ingredients list
        food = cls(ingredients=[])
        # override instance var hearts, what programer gave as input from nothing
        food.hearts = hearts
        return food



def main():
    # adding instance of Food with ingredients
    mushroom_skewer = Food(ingredients=["Mushroom", "Hearty Mushroom"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts!")
    # Food instance with from_nothing() assigning hearts value 2
    mushroom_skewer = Food.from_nothing(hearts=2)
    print(f"This skewer heals {mushroom_skewer.hearts} hearts!")

main()
