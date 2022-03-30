import storage
from list_profiles import get_profiles

#Takes in a profile name, returns false if profile is not found, otherwise returns the profile
def get_profile(name):
    if name.lower() in [profile['name'].lower() for profile in get_profiles()]:
        for profile in get_profiles():
            if profile['name'].lower() == name.lower():
                return profile

        return False #Shouldn't hit this, but just in case.
    else:
        return False


##### WIP TO GET FUNCTION WORKING. List profiles also broke #####


print(get_profile('R'))
