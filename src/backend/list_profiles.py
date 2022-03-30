import storage

def list_profiles():
    currentProfiles = [next(iter(i.values())) for i in storage.read_data()['profiles']]
    for i in currentProfiles:
        print(next(iter(i.values()))) # Iterates over each profile and prints name.


##### WIP TO GET FUNCTION WORKING #####