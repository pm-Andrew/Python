# demo4.py
# Andrew

rock_group = input("Enter a phrase: ")
# hard code: "Three Days Grace 1"

# len() is to count character in variable
# print(len(rock_group))

# if the string contains a capital letter, print it out

for character in rock_group:
    # check if the character is numeric
    if character.isnumeric():
        print(character)

    # check if the character is upper
    # if character.isupper():
        # print(character)
