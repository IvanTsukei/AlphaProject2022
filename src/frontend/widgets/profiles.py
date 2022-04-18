import tkinter as tk
from functools import partial
from tkinter import *
from tkinter import ttk

from backend.list_profiles import return_profiles

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
                        
                        foreground="black",
                        darkcolor="#737373",
                        selectbackground="#007fff",
                        lightcolor="#737373",
                        background="#737373"
                        )

        profileCombo = ttk.Combobox(state = "readonly", font="Verdana 12 bold") # Initiates the dropdown

        ### Main

        def callbackFunc(event):
            profile = event.widget.get()
            selected = select_profile_callback(profile)
            return selected

        for profile in return_profiles():
            profileCombo['values'] = tuple(list(profileCombo['values']) + [str(profile['name'])]) # Adds each profile to the dropdown list

        ### Misc
        
        label = Label(text = 'Your Profiles', fg = 'white', bg = '#1c1c1c', font="Verdana 12")
        label.grid(row = 1, column = 1)

        profileCombo.set('Select a Profile') # Sets default text
        profileCombo.grid(row = 2, column = 1)
        profileCombo.bind("<<ComboboxSelected>>", callbackFunc)


