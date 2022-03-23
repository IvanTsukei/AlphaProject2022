import json



profiles = {}

def add_profile():
    name = input()
    email = input()
    profiles[name] = {'email': email}

add_profile()

with open('profiles.json', 'w') as f:
    json.dump(profiles, f)