# Bitcoin example
# Andrew


import requests
import sys

# check if number entered
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Bitcoin quantity from C-line
try:
    qty = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# calling CoinCap API
response = requests.get("https://api.coincap.io/v2/assets/bitcoin")


# convert into python useable data
response = response.json()

price = float(response["data"]["priceUsd"])
print(f"${price * qty:,.4f}")
