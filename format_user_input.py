## How to format user data
name = input("What's your name?")
if "," in name:
    last, first = name.split(",")
    name = f"{first} {last}"

print(f"Hello {name}") 
    

    #Foramt user data with matches functionality 

# import re

# name = input("What's your nsme?").strip()

# matches = re.search(r"^(.+), *(.+)$", name)
# if matches:

#     name = matches.group(2) + " " + matches.group(1)

#     print(f"Hello {name}") 

    ### user format with single variable

""" import re

name = input("What's your nsme?").strip()

matches = re.search(r"^(.+), (.+)$", name)
if matches:

    last, first = matches.group(2) 
    name = f"{first} {last}"   
print(f"Hello {name}") """

   ### Two Variable
import re

name = input("What's your nsme?").strip()

matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)  
    name = f"{first} {last}"
print(f"Hello {name}")




   ## Usig Warlus Operator for matches
""" import re

name = input("What's your nsme?").strip()



if matches:= re.search(r"^(.+), *(.+)$", name):
   
    name = matches.group(2) + " " + matches.group(1)
   
print(f"Hello {name}") """

""" matches = re.search(r"^(.+), *(.+)$", name) """



   ### How to collect username fron twitter of users
""" url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}") """