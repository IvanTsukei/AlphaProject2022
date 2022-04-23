import tkinter as tk
from functools import partial
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.messagebox import showerror
import tkinter.font as fnt
from pathlib import Path

from backend.list_profiles import return_profiles
from backend.add_profile import add_profile
from backend.delete_profile import delete_profile

### Main

class ProfilesWidget(tk.Frame):
    def __init__(self, parent, select_profile_callback):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.configure(bg='#272c38')

        # Very much a patchwork job getting the BG image in...
        self.grid_columnconfigure(0, minsize=303)
        self.grid_columnconfigure(1, minsize=286)
        self.grid_columnconfigure(2, minsize=311)
        self.grid_rowconfigure(19, minsize=450)
        self.grid_rowconfigure(1, minsize=210)
        self.grid_rowconfigure(6, minsize=30)
        self.grid_rowconfigure(8, minsize=36)
        self.grid_rowconfigure(11, minsize=5)
        self.grid_rowconfigure(12, minsize=20)
        self.grid_rowconfigure(14, minsize=26)
        self.grid_rowconfigure(17, minsize=10)

        ### Styling

        bg = '#5f5f5f'

        style = ttk.Style()
        style.theme_use("clam")
        style.configure('TCombobox',
                        foreground = "#2a2b2c",
                        background = '#628ffa',
                        borderwidth = 2
                        )


        profileCombo = ttk.Combobox(self, state = "readonly", font="Verdana 12 bold") # Initiates the dropdown
        newProfile = tk.Text(self, height = 1, width = 22, padx=10, pady=10, foreground="#2a2b2c", bg='#628ffa', font="Verdana 12 bold", borderwidth=2) # Initiating the profile adding textbox
        deleteProfile = tk.Text(self, height = 1, width = 22, padx=10, pady=10, foreground="#2a2b2c", bg='#628ffa', font="Verdana 12 bold", borderwidth=2) # Initiating the profile deleting textbox

        # BG Image

        bgImage = Path(__file__).parent.resolve() / 'Images' / 'HomeBG.png'

        homeBGLoc = Image.open(bgImage)
        homeBG = ImageTk.PhotoImage(homeBGLoc)

        homeBGDiv = tk.Label(self, image = homeBG)
        homeBGDiv.image = homeBG
        homeBGDiv.place(x=0, y=0, relwidth=1)
        homeBGDiv.lower()
        # self.create_image(0, 0, image=homeBG, anchor = 'nw') ### This doesn't actually work, keep it commented out. Just saw create_image as a possible solution

        # # Main Div

        # maindivImage = Path(__file__).parent.resolve() / 'Images' / 'TopDivLine.png'

        # topdivlineLoc = Image.open(maindivImage)
        # topdivLine = ImageTk.PhotoImage(topdivlineLoc)

        # topplacedDiv = tk.Label(self, image = topdivLine, bg = '#272c38')
        # topplacedDiv.image = topdivLine
        # topplacedDiv.grid(row = 16, column = 1, padx=10, pady=10)

        # Diving Line Widgets

        subdivImage = Path(__file__).parent.resolve() / 'Images' / 'DividingLine.png'

        divlineLoc = Image.open(subdivImage)
        divLine = ImageTk.PhotoImage(divlineLoc)

        firstplacedDiv, secondplacedDiv = tk.Label(self, image = divLine, bg = '#272c38'), tk.Label(self, image = divLine, bg = '#272c38') # Had to break it into two since I can't place the same image across multiple rows with one cmd.
        firstplacedDiv.image = divLine
        firstplacedDiv.grid(row = 7, column = 1, padx=10, pady=10)
        secondplacedDiv.grid(row = 13, column = 1, padx=10, pady=10)
        

        # Listview Styling 
        self.option_add('*TCombobox*Listbox*Font', "Verdana 10 bold")
        self.option_add('*TCombobox*Listbox*Background', bg)
        self.option_add('*TCombobox*Listbox*Foreground', "black")
        self.option_add('*TCombobox*Listbox*selectBackground', "#FFFFFF")
        self.option_add('*TCombobox*Listbox*selectForeground', bg)

        ### Loading a Profile

        def callbackFunc(event): # Ties selection of profile to loading the profile
            profile = event.widget.get()
            selected = select_profile_callback(profile)
            return selected

        for profile in return_profiles(): # Adds each profile to the dropdown list
            profileCombo['values'] = tuple(list(profileCombo['values']) + [str(profile['name'])])

        # Visual for loading profiles

        profileCombo.set('Select a Profile') # Sets default text
        profileCombo.grid(row = 5, column = 1, padx=10, pady=10)
        profileCombo.bind("<<ComboboxSelected>>", callbackFunc)

        ### Adding a Profile

        def clear_error(value): # Removes error message.
            value.destroy()

        def profile_check_callback(widget, cmd): # Handles outputting of error messages for adding a new profile and getting the input of the text box. Also handles deleting a profile to save on space.
            userInput = widget.get('1.0', 'end-1c')
            invalidInput = Label(self, text = 'Done!', fg = 'green', bg = '#1f2631', font="Verdana 8 italic")

            try:
                if cmd == add_profile: # Lazy swap between add and delete
                    cmd(userInput, 'Skip')
                    invalidInput.grid(row = 12, column = 1)
                else:
                    cmd(userInput)
                    invalidInput.grid(row = 18, column = 1)

                self.after(2000, clear_error, invalidInput)

            except ValueError as v:
                invalidInput = Label(self, text = f'{v}', fg = 'red', bg = '#1f2631', font="Verdana 8 italic") # Creates a label for the error 
                if cmd == add_profile:
                    invalidInput.grid(row = 12, column = 1)
                else:
                    invalidInput.grid(row = 18, column = 1)
                self.after(2000, clear_error, invalidInput) # Callback to error removal. Removes after 2 sec

        # Visual for adding profile

        # newprofileLabel = Label(self, text = 'Create a New Profile', fg = 'white', bg = '#1f2631', font="Verdana 12")

        submitButton = tk.Button(self, text = 'Add Profile', fg = 'white', bg = '#6e819e', activebackground = '#50678a', font = fnt.Font(font = "Verdana 10"), command = lambda : profile_check_callback(newProfile,add_profile)) # lambda needed so function doesn't run as soon as main is run.

        # newprofileLabel.grid(row = 7, column = 1)
        newProfile.grid(row = 9, column = 1, padx=10, pady=10)
        submitButton.grid(row = 10, column = 1)

        ### Deleting a Profile

        # deleteprofileLabel = Label(self, text = 'Delete a Profile', fg = 'white', bg = '#1f2631', font="Verdana 12")
        deletesubmitButton = tk.Button(self, text = 'Delete Profile', fg = 'white', bg = '#6e819e', activebackground = '#50678a', font = fnt.Font(font = "Verdana 10"), command = lambda : profile_check_callback(deleteProfile,delete_profile))

        # deleteprofileLabel.grid(row = 12, column = 1)
        deleteProfile.grid(row = 15, column = 1, padx=10, pady=10)
        deletesubmitButton.grid(row = 16, column = 1)
