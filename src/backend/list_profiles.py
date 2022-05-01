import backend.storage as storage

def return_profiles():
    """
    Function for listing all the profiles.
    """
    currentProfiles = storage.read_data()['profiles']
    return currentProfiles
