""" name = input("What's your name?")
if "," in name:
    last, first = name.split(",")
    name = f"{first} {last}"

print(f"Hello {name}") """

""" import re

name = input("What's your nsme?").strip()

matches = re.search(r"^(.+), (.+)$", name)
if matches:
   
    name = matches.group(2) + " " + matches.group(1)
   
print(f"Hello {name}") """

""" import re

name = input("What's your nsme?").strip()

matches = re.search(r"^(.+), (.+)$", name)
if matches:

    last, first = matches.group(2) 
    name = f"{first} {last}"   
print(f"Hello {name}") """
import re

name = input("What's your nsme?").strip()

matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)  
    name = f"{first} {last}"
print(f"Hello {name}")