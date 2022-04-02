import storage

### Takes in a profile name, returns false if profile is not found, otherwise deletes the profile

def delete_profile(prof):
    data = storage.read_data()

    if prof.lower() in [profile['name'].lower() for profile in data['profiles']]:
        for profile in data['profiles']:
                if profile['name'].lower() == prof.lower():
                    profile.clear()

    storage.write_data(data)
    return True


print(delete_profile('R'))