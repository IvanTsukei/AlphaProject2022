import json
import pathlib

filePath = pathlib.Path(__file__).parent.resolve() / 'profiles.json'

profiles = {}

def add_profile():
    name = input()
    email = input()
    tickers = [input()]
    profiles[name] = {'email': email, 'ticker': tickers}

add_profile()

with open(filePath, 'a', encoding='utf8') as f:
    json.dump(profiles, f, indent=4)
f.close()