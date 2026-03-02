# Instance Methods
# Andrew

class Package:
    # dunder init method
    def __init__(self, number, sender, recipient, weight):
        # instance variables
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
    # dunder STR
    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight}kg"

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg


def main():
    ## this here is the string with the informatioin we want
    # packages = ["Package 1: Alice to Bob, 10kg", "Package 2: Bob to Charlie, 5kg"]
    # here we can take the class Package now
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight=5)
    ]
    # using a for loop
    for package in packages:
        # we are calling the instance variable (.number,.sender,.recipient)
        print(f"{package} costs ${package.calculate_cost(cost_per_kg=2)}")

main()
