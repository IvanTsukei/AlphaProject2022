from get_profile import profile_index
from get_profile import get_profile
import storage

### Takes in a profile name, returns false if profile is not found, otherwise deletes the profile

def delete_profile(name):
    data = storage.read_data()

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
        return False
    else:
        del data['profiles'][profile_index(name)]
        storage.write_data(data)
        return True


print(delete_profile('C'))