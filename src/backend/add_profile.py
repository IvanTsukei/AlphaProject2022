import json
from pathlib import Path
import re

filePath = Path(__file__).parent.resolve() / 'profiles.json' # Points to the storage area

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

with open(filePath, 'r', encoding='utf8') as f: # Opening the file for for check purposes.
    userProfiles = json.loads("[" + f.read().replace("}{", "},\n{") + "]") # Makes it so I can iterate over the contests.

def invalid_name_input(value): # Name checker.
    if len(value) == 0 or len(value) > 20:
        return "Please only enter between 0 and 20 characters."
        
    for char in value: # Checks to ensure its only alpha or space. 
        if not (char.isalpha() or char.isspace()):
            return "Please only enter letters of the Alphabet."

    for i in userProfiles: # Checks to ensure name isn't already in use.
        for profile_names in i.values():
            if value.lower() == profile_names.lower():
                return "This name is already in use."

    return False

def invalid_email_input(value):
    if not (re.fullmatch(regex, value)):
        return("Please enter a valid email.")


while True: # Loop for checking to ensure name isn't in use using function.
    name = input()
    
    if invalid_name_input(name):
        print(invalid_name_input(name))

    else:
        break

    continue

while True: # Loop for checking to ensure the email isn't in use using function.
    email = input()
    
    if email == "Skip": # Lets the user skip this step.
        email = "NA"
        break

    elif invalid_email_input(email): # Loop for checking to ensure the email is valid.
        print(invalid_email_input(email))

    else:
        break

    continue

f.close() # Closes the file since it'll be appended to soon.

profiles = {'name': name, 'email': email}

with open(filePath, 'a', encoding='utf8') as f: # Opens the file again to dump the new data to it at the end. 
    json.dump(profiles, f, indent=2)
f.close()