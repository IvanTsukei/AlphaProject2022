import json
from pathlib import Path

def file_path():
    return Path(__file__).parent.resolve() / 'profiles.json' # Points to the storage area

def read_data():
    filePath = file_path()

    with open(filePath, 'r', encoding='utf8') as f: # Opening the file for for check purposes.
        #userProfiles = json.loads("[" + f.read().replace("}{", "},\n{") + "]") # Makes it so I can iterate over the contests.
        data = json.loads(f.read())
        return data

def write_data(data):
    with open(file_path(), "w") as outFile:
        outFile.write(json.dumps(data, indent = 4))


