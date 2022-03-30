import storage
import list_profiles

def get_profile(value):

    if value.lower() in [x.lower() for x in list_profiles.all_profiles()]:
        return 
    else:
        return f"Please select an existing profile from those listed below.\n{list_profiles.all_profiles()}"


##### WIP TO GET FUNCTION WORKING. List profiles also broke #####


get_profile('1')