import tkinter as tk

from backend.get_profile import get_profile

class ProfileWidget(tk.Frame):
    def __init__(self, parent, back_callback):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.back_button = tk.Button(self, text="Back", command = back_callback)
        self.back_button.grid(row = 0, column = 0)

        self.stock_buttons = []

    def show(self, profile_name):
        profile = get_profile(profile_name)

        for button in self.stock_buttons:
            button.destroy()
        self.stock_buttons = []

        print(profile)

        i = 1
        for stock in profile['stocks']:
            button = tk.Button(self, text=stock) #ToDo: Add command and callback.
            button.grid(row = i, column = 0)
            self.stock_buttons.append(button)
            i += 1










