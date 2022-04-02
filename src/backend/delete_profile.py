from get_profile import profile_index
import storage

### Takes in a profile name, returns false if profile is not found, otherwise deletes the profile

def delete_profile(name):
    data = storage.read_data()

    del data['profiles'][profile_index(name)]

    storage.write_data(data)
    return True


print(delete_profile('R'))
