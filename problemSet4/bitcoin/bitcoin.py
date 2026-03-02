# Bitcoin Price Index
# Andrew

import requests
import sys

# check if number entered
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Bitcoin quantity from C-line correct?
try:
    # quanity of bitcoins
    qty = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# calling CoinCap API
response = requests.get("https://api.coincap.io/v2/assets/bitcoin")


# convert into python useable data
response = response.json()

# converting response to a float
price = float(response["data"]["priceUsd"])

# prints out in a $ float format
print(f"${price * qty:,.4f}")
