""" email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")

else:
    print("Invalid") """

email = input("What's your email?").strip()

username, domain = email.split("@")
if (username) and ("." in domain):
    print(username)
else:
    print("Invalid")    
