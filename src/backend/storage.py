import json
from pathlib import Path

def read_data():
    filePath = Path(__file__).parent.resolve() / 'profiles.json' # Points to the storage area

    with open(filePath, 'r', encoding='utf8') as f: # Opening the file for for check purposes.
        userProfiles = json.loads("[" + f.read().replace("}{", "},\n{") + "]") # Makes it so I can iterate over the contests.