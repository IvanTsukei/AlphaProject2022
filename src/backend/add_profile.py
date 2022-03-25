import json
import pathlib

filePath = pathlib.Path(__file__).parent.resolve() / 'profiles.json' # Points to the storage, json, file.

profiles = {}

with open(filePath, 'r', encoding='utf8') as f: # Opening the file for for check purposes.
    userProfiles = json.load(f)

def invalid_name_input(value): # Name checker.
    if len(value) == 0 or len(value) > 20:
        return "Please only enter between 0 and 20 characters."
        
    for char in value: # Checks to ensure its only alpha or space. 
        if not (char.isalpha() or char.isspace()):
            return "Please only enter letters of the Alphabet."

    for key, vall in userProfiles.items(): # Checks to ensure name isn't already in use.
        if value.lower() == key.lower():
            return "This name is already in use."

    return False

while True: # Loop for above.
    name = input()
    
    if invalid_name_input(name):
        print(invalid_name_input(name))
    else:
        break
    continue

f.close() # Closes the file since it'll be appended to soon.

def add_profile(): # Main adder
    email = input()
    profiles[name] = {'email': email}

add_profile()

with open(filePath, 'a', encoding='utf8') as f: # Opens the file again to dump the new data to it at the end. 
    json.dump(profiles, f, indent=4)
f.close()