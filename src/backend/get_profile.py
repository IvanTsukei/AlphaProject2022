import json
from backend.storage import read_data
from pathlib import Path

filePath = Path(__file__).parent.resolve() / 'profiles.json' # Points to the storage area

with open(filePath, 'r', encoding='utf8') as f: # Opening the file for for check purposes.
    userProfiles = json.loads("[" + f.read().replace("}{", "},\n{") + "]") # Makes it so I can iterate over the contests.

currentProfiles = [next(iter(i.values())) for i in userProfiles] # Pulls all the profiles names.

def invalid_profile_input(value):
    if value.lower() in currentProfiles.lower():
        return False
    else:
        return f"Please select an existing profile from those listed below.\n{currentProfiles}"

while True: # Loop for checking to ensure profile name exists.
    profile_selection = input()
    
    if invalid_profile_input(profile_selection):
        print(invalid_profile_input(profile_selection))

    else:
        break

    continue
