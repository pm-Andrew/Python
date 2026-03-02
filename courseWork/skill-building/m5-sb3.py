# m5-sb3.py
# Andrew



import random  # import the random library
from pyfiglet import Figlet  # import Figlet from pyfiglet

figlet = Figlet()  # Create an a Figlet object

fonts = figlet.getFonts()  # Get list of fonts from figlet
font = random.choice(fonts)  # Use the random.choice() method to get font list
figlet.setFont(font=font)  # Set the current font to use to the randomly chosen one

text = input("Enter some text: ")  # Ask user for input

print(figlet.renderText(text))  # Use the figlet.renderText() method to print out text

"""
--Alt Way--
figletText = figlet.renderText(text)
print(figletText)
"""
