import json
import pathlib

filePath = pathlib.Path(__file__).parent.resolve() / 'profiles.json'

with open(filePath, 'r', encoding='utf8') as f:
    profiles = json.load(f)

for key, value in profiles.items():
    print(key)