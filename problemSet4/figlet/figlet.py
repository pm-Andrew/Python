# Problem 2: Frank, Ian and Glen’s Letters figlet.py
# Andrew

# Problem 2: Frank, Ian and Glen’s Letters figlet.py
# Andrew


"""
# User input w/ zero or two command-line arguments

# if 0 the user would like a random font

# if 2 the user would like to output text in a specific font,[ -f or --font | Font ]
    # if [ -f or --font ] are not the first arg. or the second arg. isn't a font name
    # exit system - "Invalid usage"

# Prompt user for input
"""
# Import random and Figlet
import sys
import random
from pyfiglet import Figlet

# Create a Figlet object
figlet = Figlet()
# get list of fonts from figlet
fonts = figlet.getFonts()

# if 0 the user would like a random font
if len(sys.argv) == 1:
    #
    # access random fonts
    font = random.choice(fonts)
    # Sets current font
    figlet.setFont(font=font)
    # ask for user input
    text = input("Input: ")
    # random text
    print(figlet.renderText(text))
    #

# if 2 arguments in command-line exit program
elif len(sys.argv) == 2:
    sys.exit("Invalid usage")

# if 2 the user would like to output text in a specific font,[ -f or --font | valid font ]
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in fonts):
    # is font name in font list
    #
    # if so ask for input
    text = input("Input: ")
    # Setting current font
    figlet.setFont(font=sys.argv[2])
    # print out in font requested
    print(figlet.renderText(text))
    #
# if anything else leave
else:
    sys.exit("Invalid usage")
