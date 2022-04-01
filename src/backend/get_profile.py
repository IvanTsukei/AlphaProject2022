from list_profiles import return_profiles

### Takes in a profile name, returns false if profile is not found, otherwise returns the profile

def get_profile(name):
    if name.lower() in [profile['name'].lower() for profile in return_profiles()]:
        for profile in return_profiles():
            if profile['name'].lower() == name.lower():
                return profile

        return False #Shouldn't hit this, but just in case.
    else:
        return "Please enter a valid profile name."