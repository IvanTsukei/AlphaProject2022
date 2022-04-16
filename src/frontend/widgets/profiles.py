import tkinter as tk
from functools import partial

from backend.list_profiles import return_profiles

class ProfilesWidget(tk.Frame):
    def __init__(self, parent, select_profile_callback):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.profile_buttons = []

        i = 0
        for profile in return_profiles():
            button = tk.Button(self, text=profile['name'], command = partial(select_profile_callback, profile['name']))
            button.grid(row = i, column = 0)
            self.profile_buttons.append(button)
            i += 1





