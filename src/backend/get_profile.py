import json
from pathlib import Path

filePath = Path(__file__).parent.resolve() / 'profiles.json' # Points to the storage area

with open(filePath, 'r', encoding='utf8') as f: # Opening the file for for check purposes.
    userProfiles = json.loads("[" + f.read().replace("}{", "},\n{") + "]") # Makes it so I can iterate over the contests.


profile_selection = input()

for i in userProfiles:
    if profile_selection in (next(iter(i))):
        print("Test")
    else:
        print("Please select an existing profile.")