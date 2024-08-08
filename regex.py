     #Getting user inour and trying to validate it.
""" email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")

else:
    print("Invalid") """
   
   #making more precise our condition

""" email = input("What's your email?").strip()

username, domain = email.split("@")
if (username) and ("." in domain):
    print(username)
else:
    print("Invalid")  """   

          #using end.switch()
""" email = input("What's your email?").strip()

username, domain = email.split("@")

if username and domain.endswith(".com"):
    print(username)
else:
    
    print(f"{email} is Invalid") """
     #Using re library

""" import re

email = input("What's your email?").strip()

if re.search("@", email):
    username, domain = email.split("@")
    print(username)
else:
    print(f"{email}: Invalid email address") """

      #using re patterns (".*" combination) to match user input
""" import re

email = input("What's your email?").strip()

if re.search(".*@.*", email):
    username, domain = email.split("@")
    print(email)
else:
    print("Invalid") """

    #for re library using (".+") combination
""" import re

email = input("What's your name?").strip() """
     #.+ combination

""" if re.search(".+@.+", email):
    print(email)
else:
    print("Invalid") """
   #.edu combination
""" if re.search(".+@.+.edu", email):
    print(email)
else:
    print("Invalid") """
    #"\.edu" combination
""" if re.search(r".+@.+\.edu", email):
    print(email)
else:
    print("Invalid") """

  #To REmove start and user input spaces, we will use "^$"

import re

email = input("What's your email?").strip().lower()

""" if re.search(r"^.+@.+\.edu$", email): """
""" if re.search(r"^..*@..*'\.'edu$", email): """

""" if re.search(r"^[^@]@[^@]'\.'edu$", email): """
""" if re.search(r"^[a-zA-Z0-9_]+@[azA-Z0-9_]\.edu$", email): """
""" if re.search(r"^\w+@\W\.(com|edu|hotmail|gov|net|org)$", email): """
   #How to remove white space
if re.search(r"^(\w\S)+@\W+\.edu$", email):
    print(email)
else:
    print("Invalid")





