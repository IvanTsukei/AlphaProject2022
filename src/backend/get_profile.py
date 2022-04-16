from backend.list_profiles import return_profiles

### Takes in a profile name, returns false if profile is not found, otherwise returns the profile

def get_profile(name):
    if name.lower() in [profile['name'].lower() for profile in return_profiles()]:
        for profile in return_profiles():
            if profile['name'].lower() == name.lower():
                return profile

        return False #Shouldn't hit this, but just in case.
    else:
        return "Please enter a valid profile name."

def profile_index(name):
    profiles = return_profiles()
    if name.lower() in [profile['name'].lower() for profile in profiles]:
        for i in range(len(profiles)):
            if profiles[i]['name'] == name:
                return i
        return False
    return "Please enter a valid profile name."

def profile_exists(name):
    return name.lower() in [profile['name'].lower() for profile in return_profiles()]


