# response.py
# Andrew

# import validators library
import validators

# getting email from user
email = input("What's your email address? ").strip()

# using validator in a conditional to catch valid emails
if validators.email(email):
    # if valid email splitting the email into username and domain at the "@"
    username, domain = email.split("@")
    print("Valid")
# Invalid email
else:
    print("Invalid")
