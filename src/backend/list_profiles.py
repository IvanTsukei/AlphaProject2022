import backend.storage as storage

def return_profiles():
    currentProfiles = storage.read_data()['profiles']
    return currentProfiles
