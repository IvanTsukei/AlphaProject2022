import json
from pathlib import Path


profiles = {}

def add_profile():
    name = input()
    email = input()
    tickers = [input()]
    profiles[name] = {'email': email, 'ticker': tickers}

add_profile()

print(profiles)


output_path = '/AlphaProject2022/src/backend'
with open(output_path, 'a', encoding='utf8') as f:
    json.dump(profiles, f, indent=4)
f.close()