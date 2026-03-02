# add.py
# Andrew

import random

def sum_numbers(a,b):
    return a + b


def random_player_name():
    names = ['Uhhhh','Rudy','Aaron','George','Theodore','Tyler','Missy']
    return random.choice(names)

def main():
    a = 'bruce'
    b = 7
    print(sum_numbers(a,b))

if __name__ == '__main__':
    main()
