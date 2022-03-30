import storage

def all_profiles():
    currentProfiles = [next(iter(i.values())) for i in storage.read_data()['profiles']]
    return currentProfiles
##### WIP TO GET FUNCTION WORKING #####