""" email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")

else:
    print("Invalid") """

""" email = input("What's your email?").strip()

username, domain = email.split("@")
if (username) and ("." in domain):
    print(username)
else:
    print("Invalid")  """   


""" email = input("What's your email?").strip()

username, domain = email.split("@")

if username and domain.endswith(".com"):
    print(username)
else:
    
    print(f"{email} is Invalid") """

import re

email = input("What's your email?").strip()

if re.search("@", email):
    username, domain = email.split("@")
    print(username)
else:
    print(f"{email}: Invalid email address")

