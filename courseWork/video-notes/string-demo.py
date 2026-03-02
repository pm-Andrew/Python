# String Methods
# https://docs.python.org/3/library/stdtypes.html#string-methods

drummerName = "Bruce Elgort"

# .lower(Prints lowercase)

print(drummerName.lower())

# .upper(Prints uppercase)
# .islower(detect in if statements)
# .isupper(detect in if statements)

for letter in drummerName:
    if the letter.isupper():
        print("Yep, that letter is uppercase")
# utput: Yep, that letter is uppercase

# .strip() 	.rstrip(only remove space on the right)	.lstrip(only remove space on the left)
drummerName = "Bruce Elgort"
print(len(drummerName.strip())) # how long is that string?
# Output: 12

# Other Handy String Methods

# .endswith()
# .startswith()
drummerName = "Bruce Elgort"
if drummerName.endswith("ort")
    print("Yep, it ends with ort")
# Output : Yep, it ends with ort


drummerName = "Bruce Elgort"
if drummerName.startswith("Bru")
    print("Yep, it ends with Bru")
else:
    print("Nope, does not start with Bru")
# Output : Yep, it ends with Bru


drummerName = "Bruce Elgort"
if drummerName.lower().startswith("bru")
    print("Yep, it ends with Bru")
else:
    print("Nope, does not start with Bru")
# Output : Yep, it ends with Bru


# .isdigit( check if number)
drummerAge = "59"

if drummerAge.isdigit():
    print("Yep, it's a number")
else:
    print(":(")

# .isaplpha( check if letters)
drummerName = "Bruce Elgort"

if drummerName.isalpha():
    print("Yep, it's letters a-z")
else:
    print(":(")

# .isalnum( checks if number or letter)
drummerName = "Bruce Elgort"

if drummerName.isalnum():
    print("Yep, it's letters a-z and numbers 0-9")
else:
    print(":(")
