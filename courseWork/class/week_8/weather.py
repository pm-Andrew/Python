# Weather Data weather.py
# Andrew

'''
In this assignment, you will create a command-line Python application that retrieves weather data from an external JSON file.
Your program will:

Fetch and parse weather data from a remote source.
Display a list of available ZIP codes if no ZIP code is provided.
Allow the user to enter a ZIP code as a command-line argument and display the corresponding weather information.
Handle errors gracefully, ensuring the program does not crash if an invalid ZIP code is entered.
This program must be run exclusively from the command line.
'''
import requests
import json
import sys
import random


response = requests.get("https://raw.githubusercontent.com/belgort-clark/ctec-121-json/refs/heads/main/weather.json")

z = response.json()
for result in z["results"]:
    print(results["zip_code"])

# zipCode =
# # check if user entered a zip code in command-line
# if len(sys.argv) == 1:
#     RndmZip = random.choice(zipCode)
