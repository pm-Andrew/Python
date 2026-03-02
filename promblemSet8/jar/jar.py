# Cookie jar.py
# Andrew S


class Jar:
    # If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
    def __init__(self, capacity=12):

        # Creating capacity
        if capacity >= 0:
            # assign variables
            self._capacity = capacity
            # current jar size
            self._size = 0
        else:
            raise ValueError


    def __str__(self):
        # should return a str with  🍪, where is the number of cookies in the cookie jar. For instance,
        # if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
        return self._size * "🍪"

    def deposit(self, deposit):
        # should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity,
        # though, deposit should instead raise a ValueError.
        if deposit <= 0:
            raise ValueError("Negative Input not Accepted")
        # deposit + cookie currently in less than capacity
        elif deposit + self.size > self.capacity:
            # finding the difference
            raise ValueError(f"Too many cookies")
        self._size = self._size + deposit



    def withdraw(self, withdraw):
        # should remove n cookies from the cookie jar. Nom nom nom.
        # If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
        if withdraw > self._size:
            raise ValueError(f"Not enough cookies to withdraw, only {self._size} cookies.")
        # current n of cookies being taken out
        self._size = self._size - withdraw

    @property
    def capacity(self):
        #  should return the cookie jar’s capacity.
       return self._capacity

    @property
    def size(self):
        # should return the number of cookies actually in the cookie jar.
        return self._size

def main():
    # the Jar has 10
    jar = Jar(10)
    # deposit 9
    jar.deposit(9)
    # withdrawl of 8
    jar.withdraw(8)
    print(jar)


if __name__ == "__main__":
    main()
