# Shirt.py
# Andrew


# Importing Image and ImageOps from Pillow,
from PIL import Image, ImageOps
# importing command-line arguments
import sys
# to deal with files and folders
import os


def main():
    # less than 3 command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # more than 3 command-line arguments
    if len(sys.argv) > 3:
        sys.exit("Too many commmand-line arguments")
    # if exactly 3 split the file name by name and extension type
    if len(sys.argv) == 3:
        # store split extensions
        file1 = os.path.splitext(sys.argv[1])
        # store split extension
        file2 = os.path.splitext(sys.argv[2])
        # Checks if file1 is a ".jpg" or ".png"
        if file1[1].lower() != ".jpg" and file1[1].lower() != ".png":
            # if not print
            print("Invalid input")
            # and Exit program
            sys.exit("Invalid input")
        # Checks if file2 is a ".jpg" or ".png"
        if file2[1].lower() != ".jpg" and file2[1].lower() != ".png":
            # if not print
            print("Invalid input")
            # and Exit program
            sys.exit("Invalid input")
        # Checks if file1 & file2 are the same file type
        if file1[1].lower() != file2[1].lower():
            # if not Exit and display message
            sys.exit("Files must have the same extension")

        # opening shirt.png and storing it to shirt variable
        shirt = Image.open("shirt.png")
        # try opening file
        try:
            # assign image to before to edit
            before = Image.open(sys.argv[1])
            # if unavalible Exit system
        except IOError:
            sys.exit("Input file does not exist")

        # editting the image using .fit()
        before = ImageOps.fit(
            # resize and crop: (w,h) resample using bucubic interpole, no border, center picture
            before, (600, 600), method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5)
        )

        # pasting shirt to second image
        before.paste(shirt, shirt)
        # saving to a new file
        before.save(sys.argv[2])
        # Exit program
        sys.exit(0)


main()
