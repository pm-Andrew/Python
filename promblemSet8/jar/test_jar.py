from jar import Jar


def test_init():
    jar = Jar()
    assert jar._capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    

def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(7)
    assert str(jar) == "🍪🍪🍪"
