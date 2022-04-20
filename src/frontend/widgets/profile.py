import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.messagebox import showerror
import tkinter.font as fnt
from pathlib import Path

from backend.get_profile import get_profile
from backend.add_stock_to_profile import add_stock
from backend.delete_stock_from_profile import delete_stock
from backend.get_stock import stock_marketcap, stock_pe, stock_industry, stock_volume, ticker_region, ticker_full_name

### Main

class ProfileWidget(tk.Frame):
    def __init__(self, parent, back_callback):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.back_button = tk.Button(self, text="Back", fg = 'white', bg = '#6e819e', activebackground = '#50678a', font = fnt.Font(font = "Verdana 10"), command = back_callback)
        self.back_button.grid(row = 0, column = 0, sticky = "nw")
        self.configure(bg='#272c38')
        self.grid_columnconfigure(0, minsize=343)
        self.grid_columnconfigure(2, minsize=347)
        self.grid_rowconfigure(10, minsize=748) # Extend widget to full canvas size
        self.grid_rowconfigure(2, minsize=65) # To move stock list down

        self.stock_buttons = []


    def show(self, profile_name):
        profile = get_profile(profile_name)
        profileName = profile['name'] # Needed to get the actual profile name

        if (hasattr(self, 'addstockLabel')): # Clears the empty list label
            self.addstockLabel.destroy()
        
        if (hasattr(self, 'addprofileLabel')): # Clears the empty list label
            self.addprofileLabel.destroy()

        ### Showing Profile Name in Top Right

        self.addprofileLabel = Label(self, text = f'Profile: {profileName}', fg = 'white', bg = '#242c3b', font="Verdana 11 italic")
        self.addprofileLabel.grid(row = 0, column = 2, sticky = "ne", pady=2)

        ### Styling

        newStock = tk.Text(self, height = 1, width = 22, padx=10, pady=10, foreground="white", bg='#628ffa', font="Verdana 12 bold", borderwidth=2) # Initiating the stock adding textbox
        deleteStock = tk.Text(self, height = 1, width = 22, padx=10, pady=10, foreground="white", bg='#628ffa', font="Verdana 12 bold", borderwidth=2) # Initiating the stock deleting textbox
        graphButton = tk.Button(self, text = 'Start Portfolio Analysis', fg = 'white', bg = '#6e819e', activebackground = '#50678a', font = fnt.Font(font = "Verdana 10"))
        

        # BG Image

        bgImage = Path(__file__).parent.resolve() / 'Images' / 'ProfileBG.png'

        homeBGLoc = Image.open(bgImage)
        homeBG = ImageTk.PhotoImage(homeBGLoc)

        homeBGDiv = tk.Label(self, image = homeBG)
        homeBGDiv.image = homeBG
        homeBGDiv.place(x=0, y=0, relwidth=1)
        homeBGDiv.lower()


        # Diving Line Widgets

        subdivImage = Path(__file__).parent.resolve() / 'Images' / 'DividingLine.png'

        divlineLoc = Image.open(subdivImage)
        divLine = ImageTk.PhotoImage(divlineLoc)
        divLine2 = ImageTk.PhotoImage(divlineLoc)

        firstplacedDiv, secondplacedDiv= tk.Label(self, image = divLine, bg = '#1f2631'), tk.Label(self, image = divLine, bg = '#1f2631')
        firstplacedDiv.image, secondPlacedDiv = divLine, divLine
        firstplacedDiv.grid(row = 4, column = 1, padx=5, pady=5)
        secondplacedDiv.place(x = 633, y = 249)


        stocksectionLabel = Label(self, text = 'Stocks in Profile', fg = 'white', bg = '#1f2631', font="Verdana 12")
        stocksectionLabel.grid(row = 3, column = 1, padx=5, pady=5)

        # Main Div

        maindivImage = Path(__file__).parent.resolve() / 'Images' / 'MiscPinkDiv.png'

        topdivlineLoc = Image.open(maindivImage)
        topdivLine = ImageTk.PhotoImage(topdivlineLoc)

        topplacedDiv = tk.Label(self, image = topdivLine, bg = '#1f2631')
        topplacedDiv.image = topdivLine
        topplacedDiv.place(x = 610, y = 414)
        
        ### Individual Stocks

        for button in self.stock_buttons:
            button.destroy()
        self.stock_buttons = []

        i = 4
        for stock in profile['stocks']:
            button = tk.Button(self, text=stock,  fg = 'white', bg = '#6390fa', activebackground = '#30467b', font = fnt.Font(font = "Verdana 10")) #ToDo: Add command and callback.
            i += 1
            button.grid(row = i, column = 1, padx=5, pady=5)
            self.stock_buttons.append(button)

        if i == 4: # QOL notif. if no stocks.
            self.addstockLabel = Label(self, text = 'No stocks in profile.\n Add some on the right!', fg = 'red', bg = '#1f2631', font="Verdana 10 italic")
            self.addstockLabel.grid(row = 5, column = 1, padx=5, pady=5)


        ### Adding a stock

        def clear_error(value): # Removes error message.
            value.destroy()

        def profile_check_callback(widget, cmd): # Handles outputting of error messages for adding a new profile and getting the input of the text box. Also handles deleting a profile to save on space.
            userInput = widget.get('1.0', 'end-1c')

            invalidInput = Label(self, text = 'Done!', fg = 'green', bg = '#1f2631', font="Verdana 10 italic")

            try:
                if cmd == add_stock: # Lazy swap between add and delete
                    cmd(profileName, userInput)
                    invalidInput.place(x = 711, y = 226)
                else:
                    cmd(profileName, userInput)
                    invalidInput.place(x = 711, y = 391)

                self.after(2000, clear_error, invalidInput)

            except ValueError as v:
                invalidInput = Label(self, text = f'{v}', fg = 'red', bg = '#1f2631', font="Verdana 10 italic") # Creates a label for the error 
                if cmd == add_stock:
                    invalidInput.place(x = 618, y = 226)
                else:
                    invalidInput.place(x = 618, y = 391)

                self.after(2000, clear_error, invalidInput) # Callback to error removal. Removes after 2 sec

        # Visual for adding stock

        newstockLabel = Label(self, text = 'Add a Stock', fg = 'white', bg = '#1f2631', font="Verdana 12")
        submitButton = tk.Button(self, text = 'Add Stock', fg = 'white', bg = '#6e819e', activebackground = '#50678a', font = fnt.Font(font = "Verdana 10"), command = lambda : profile_check_callback(newStock,add_stock)) # lambda needed so function doesn't run as soon as main is run.

        # newstockLabel.place(x = 680, y = 40)
        newStock.place(x = 598, y = 137) #### using place since the auto resize of rows makes it a mess
        submitButton.place(x = 693, y = 189)

        ### Deleting a stock

        deletestockLabel = Label(self, text = 'Delete a Stock', fg = 'white', bg = '#1f2631', font="Verdana 12")
        submitdeleteButton = tk.Button(self, text = 'Delete Stock', fg = 'white', bg = '#6e819e', activebackground = '#50678a', font = fnt.Font(font = "Verdana 10"), command = lambda : profile_check_callback(deleteStock,delete_stock)) # lambda needed so function doesn't run as soon as main is run.
        
        # deletestockLabel.place(x = 670, y = 205)
        deleteStock.place(x = 598, y = 302)
        submitdeleteButton.place(x = 683, y = 354)

        graphButton.place(x = 651, y = 452)
        
        
        '''
        To add: clicking on a individual stock will give fullname and basic markit info. Everything under backend.get_stock. 

        Combobox again in a different column for the actual selection of chart stuff along with chart settings. 
        Clicking a option in the combobox would change the options people have below it for the color/line type/etc.
        A "graph it" button would then show the charts on a new screen.

        Two back button options here, one back to the same profile and another to home page (or just back to home)


        Need 

        Have the blue banner at the top of column 1 with the name of the profile?

        '''