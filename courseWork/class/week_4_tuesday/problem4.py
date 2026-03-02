# problem4.py
# Andrew

"""
Create a program that converts an amount from one currency to another. Prompt the user for the amount, the source currency, and the target currency in the format amount source target (e.g., 100 USD EUR). Assume fixed exchange rates (e.g., 1 USD = 0.85 EUR, 1 USD = 110 JPY).

For example:
- Input: 100 USD EUR
- Output: 85.0 EUR
"""

data = input("Enter Amount Currency 'Currencey to Conver to': ")

amount, input_currency, output_currency = data.split(" ")
amount = float(amount)

if input_currency == "USD" and output_currency == "EUR":
    print(f"{amount * .85} {output_currency}")
elif input_currency == "EUR" and output_currency == "USD":
    print(f"{amount * 1.04} {output_currency}")
elif input_currency == "USD" and output_currency == "YEN":
    print(f"{amount * 155.53} {output_currency}")
elif input_currency == "YEN" and output_currency == "EUR":
    print(f"{amount * 155.53} {output_currency}")
