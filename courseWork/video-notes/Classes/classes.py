 # classes
# https://www.youtube.com/watch?v=PuxM0hR32GA


class Package:
    # dunder init method
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

def main():
    ## this here is the string with the informatioin we want
    # packages = ["Package 1: Alice to Bob, 10kg", "Package 2: Bob to Charlie, 5kg"]
    # here we can take the class Package now
    
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight=5)
    ]

main()

# More in class-int-variables.py
