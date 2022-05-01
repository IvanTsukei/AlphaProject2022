import re
import backend.storage as storage

#Adds profile to profiles if it passes checks
#If it doesn't pass checks, returns false, otherwise returns true

def add_profile(name, email):
    """
    Function for adding a new profile.
    """

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    currentProfiles = storage.read_data()['profiles']

    def invalid_name_input(name):
        """
        Checks if the profile name is valid.
        """
        if len(name) == 0 or len(name) > 20:
            raise ValueError ("Please only enter between 0 and 20 characters.")
            
        for char in name: # Checks to ensure its only alpha or space.
            if not (char.isalpha() or char.isspace()):
                raise ValueError ("Please only enter letters of the Alphabet.")


        if name in [profile['name'] for profile in currentProfiles]: # Checks to ensure name isn't already in use
            raise ValueError ("This name is already in use.")

        return False

    def invalid_email_input(value):
        """
        Checks if the email is valid.
        """
        if not (re.fullmatch(regex, value)):
            raise ValueError ("Please enter a valid email.")

    ## Name Checker

    if invalid_name_input(name):
        print(invalid_name_input(name))
        return False

    ## Email Checker

    if email == "Skip": # Lets user skip this step
        email = "NA"

    elif invalid_email_input(email): # Checks if the email is valid
        print(invalid_email_input(email))
        return False

    ## Writing to profiles.json

    data = storage.read_data()
    data['profiles'].append({'name': name, 'email': email, 'stocks': []})
    storage.write_data(data)
    return True
