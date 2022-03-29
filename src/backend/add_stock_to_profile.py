import json
from xml.etree.ElementTree import TreeBuilder
import storage
from pathlib import Path

filePath = Path(__file__).parent.resolve() / 'profiles.json' # Points to the storage area

with open(filePath, 'r', encoding='utf8') as f: # Opening the file for for check purposes.
    userProfiles = json.loads("[" + f.read().replace("}{", "},\n{") + "]") # Makes it so I can iterate over the contests.

currentProfiles = [next(iter(i.values())) for i in userProfiles] # Pulls all the profiles names.

while True:
    stocks = input()

    if stocks == "Quit" or "quit":
        break
    else:
        userProfiles["stocks"].append(stocks)
        continue
