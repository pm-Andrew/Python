# Comparing String 2 str-comp2.py
# Bruce Elgot / Andrew
#

def compare_strings():
    # Declare two variables that are strings
    string1 = 'Bruce'
    string2 = 'Gayle'

    # Is string1 greater than string 2?
    if string1 > string2:
        print('"Bruce" is greater than "Gayle"')
    else:
        print('"Gayle" is greater than "Bruce"')
    print('But why is that?\nLets have a look...\n\n')

    # set up two varab;es that will accumulate values of letter in each string
    valueOfString1 = 0
    valueOfString2 = 0

    print('Sting:', string1)
    print('_' * 80)
    # Iterate through sting1, one character at a time
    for character in string1:
        print('Value of character', character, 'is', ord(character))
        # Accumlate ASCII values of each character
        valueOfString1 = valueOfString1 = ord(character)
    print('The total value of each of the ASCII characters for "' + string1 + '" is:', valueOfString1)

    print('\n'*3)
    print('String:', string2)
    print('_' * 80)
    # Iterate through sting1, one character at a time
    for character in string2:
        print('Value of character', character, 'is', ord(character))
        # Accumlate ASCII values of each character
        valueOfString2 = valueOfString2 = ord(character)
    print('The total value of each of the ASCII characters for "' + string2 + '" is:', valueOfString2)

    # Display results
    print('\n'*2)
    print('Value of string1 = "' + string1 + '" is', valueOfString1)
    print('Value of string2 = "' + string2 + '" is', valueOfString2)
compare_strings()
