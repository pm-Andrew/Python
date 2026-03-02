# Instance Variabes
# Andrew

class Package:
    # dunder init method
    def __init__(self, number, sender, recipent, weight):
        self.number = number
        self.sender = sender
        self.recipent = recipent
        self.weight = weight

def main():
    ## this here is the string with the informatioin we want
    # packages = ["Package 1: Alice to Bob, 10kg", "Package 2: Bob to Charlie, 5kg"]
    # here we can take the class Package now
    packages = [
        Package(number=1, sender="Alice", recipent="Bob", weight=10),
        Package(number=2, sender="Bob", recipent="Charlie", weight=5)
    ]
    # using a for loop
    for package in packages:
        # we are calling the instance variable (.number)
        print(f"Package {package.number}: {package.sender} to {package.recipent}, {package.weight}kg")

main()
