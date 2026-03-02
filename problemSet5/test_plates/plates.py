# plates.py 2.0
# Andrew


def main():
    # Get input from the user
    plate = input("Plate: ")
    # Call the is_vaild() function w/ the plate entered
    if is_valid(plate):
        # plate is vaild since is_valid() returned True
        print("Valid")
    else:
        # print is not valid since is_valid() returned False
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False


    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False


    for character in s:
        # Chcek to make its a number or letter
        # If (.,-) etc. return false
        if character.isalnum() == False:
            return False


    firstNumber = True

    # Lopo through each character
    for i in range(len(s)):
        # if the character is a number
        if s[i].isdigit():
            # Use string slicing to get everthing to the right in the plate including
            # the current character to see if it's not a number
            # This will check to see if there happens to be a letter on the end
            # which is not allowed
            if not s[i:].isdigit():
                # There must have been a letter at the end which is invalid
                return False

            # This conditional will check to see if the character is a zero
            # 0's allowed but not as the first number
            if s[i] == "0" and firstNumber == True:
                return False
            else:
                # Now that the fisrtNumber was not in fact 0 we set the firstNUmber to false
                firstNumber = False

    return True

if __name__ == "__main__":
    main()
