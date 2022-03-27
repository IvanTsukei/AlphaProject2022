import json
import pathlib

filePath = pathlib.Path(__file__).parent.resolve() / 'profiles.json'

with open(filePath, 'r', encoding='utf8') as f: # Opening the file for for check purposes.
    userProfiles = json.loads("[" + f.read().replace("}{", "},\n{") + "]") # Makes it so I can iterate over the contests.

for i in userProfiles:
    print(next(iter(i.values()))) # Iterates over each profile and prints name.