from list_profiles import return_profiles
import get_profile
import storage

### Takes in a profile name, returns false if profile is not found, otherwise deletes the profile

def delete_profile(profile):
    data = get_profile.get_profile(profile).clear()
    storage.write_data(data)


print(delete_profile('R'))