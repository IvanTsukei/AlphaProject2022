from backend.get_profile import profile_index
from backend.get_profile import get_profile
import backend.storage as storage

### Takes in a profile name, returns false if profile is not found, otherwise deletes the profile

def delete_profile(name):
    data = storage.read_data()

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
        raise ValueError ("Please enter a valid profile name.")
    else:
        del data['profiles'][profile_index(name)]
        storage.write_data(data)
        return True

