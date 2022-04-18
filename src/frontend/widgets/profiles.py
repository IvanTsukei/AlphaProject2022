import tkinter as tk
from functools import partial
from tkinter import *
from tkinter import ttk

from backend.list_profiles import return_profiles
from backend.add_profile import add_profile

class ProfilesWidget(tk.Frame):
    def __init__(self, parent, select_profile_callback):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.profile_buttons = []

        ### Styling

        style = ttk.Style()
        style.theme_use("clam")
        style.configure('TCombobox',
                        fieldbackground="orange",
                        relief='sunken',
                        foreground="black",
                        darkcolor="#737373",
                        selectbackground="#007fff",
                        lightcolor="#737373",
                        background="#737373",
                        borderwidth=2
                        )

        profileCombo = ttk.Combobox(state = "readonly", font="Verdana 12 bold") # Initiates the dropdown

        ### Loading a Profile

        def callbackFunc(event):
            profile = event.widget.get()
            selected = select_profile_callback(profile)
            return selected

        for profile in return_profiles():
            profileCombo['values'] = tuple(list(profileCombo['values']) + [str(profile['name'])]) # Adds each profile to the dropdown list

        ### Misc
        
        profilesLabel = Label(text = 'Your Profiles', fg = 'white', bg = '#1c1c1c', font="Verdana 12")
        profilesLabel.grid(row = 1, column = 1)

        profileCombo.set('Select a Profile') # Sets default text
        profileCombo.grid(row = 2, column = 1)
        profileCombo.bind("<<ComboboxSelected>>", callbackFunc)

        ### Adding a Profile

        newProfile = tk.Text(height = 2, width = 25, foreground="black", bg='#737373', font="Verdana 12 bold", relief='sunken', borderwidth=2)
        # newProfile.set('Enter the Profile Name') # Sets default text

        newprofileLabel = Label(text = 'Create a New Profile', fg = 'white', bg = '#1c1c1c', font="Verdana 12")

        userInput = newProfile.get(1.0, 'end-1c')
        submitButton = tk.Button(text = 'Add Profile', command = add_profile(userInput, 'Skip'))


        newprofileLabel.grid(row = 4, column = 1)
        newProfile.grid(row = 5, column = 1)
        submitButton.grid(row = 6, column = 1)
