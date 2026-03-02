# Checking a Dictionary for a Key m4-sb1.py
# Andrew


"""
Create a dictionary named toys.
The dictionary should have the name of a toy as the key, and the value should be the location of that toy.
Ask the user to input the name of a toy and then print out its location.
If the toy is found in the dictionary, print out its name and location.
If it's not found, be sure to use a try/except to catch the error (KeyError)

"""
toys = {
    "Nerf Shotgun": "Hanging by hats",
   "Lightsabers": "Top of bookcase",
    "Legos": "All over living room"
}

def main():
    toy = input("Pick a toy: \n Nerf Shotgun \n Lightsabers \n Legos \n ---------\n toy:")
    toy = toy.title()
    try: # perfect world
        print(toy, toys[toy])


    except KeyError: # If not in dictionary
        print("Read the options again")



main() # this can easily be expanded to do a lower case KeyError if wanted
