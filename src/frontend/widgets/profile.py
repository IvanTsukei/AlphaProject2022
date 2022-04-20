import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.messagebox import showerror
import tkinter.font as fnt
from pathlib import Path

from backend.get_profile import get_profile
from backend.add_stock_to_profile import add_stock
from backend.get_stock import stock_marketcap, stock_pe, stock_industry, stock_volume, ticker_region, ticker_full_name

### Main

class ProfileWidget(tk.Frame):
    def __init__(self, parent, back_callback):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.back_button = tk.Button(self, text="Back", fg = 'white', bg = '#6e819e', activebackground = '#50678a', font = fnt.Font(font = "Verdana 10"), command = back_callback)
        self.back_button.grid(row = 0, column = 0, sticky = "nw")
        self.configure(bg='#272c38')
        self.stock_buttons = []

    def show(self, profile_name):
        profile = get_profile(profile_name)

        ### Styling

        newStock = tk.Text(self, height = 1, width = 22, padx=10, pady=10, foreground="white", bg='#5f5f5f', font="Verdana 12 bold", borderwidth=2) # Initiating the stock adding textbox

        # Diving Line Widgets

        subdivImage = Path(__file__).parent.resolve() / 'Images' / 'DividingLine.png'

        divlineLoc = Image.open(subdivImage)
        divLine = ImageTk.PhotoImage(divlineLoc)

        firstplacedDiv = tk.Label(self, image = divLine, bg = '#272c38')
        firstplacedDiv.image = divLine
        firstplacedDiv.grid(row = 2, column = 0, padx=5, pady=5)


        stocksectionLabel = Label(self, text = 'Stocks in Profile', fg = 'white', bg = '#272c38', font="Verdana 12")
        stocksectionLabel.grid(row = 1, column = 0, padx=5, pady=5)
        
        ### Individual Stocks

        for button in self.stock_buttons:
            button.destroy()
        self.stock_buttons = []

        i = 2
        for stock in profile['stocks']:
            button = tk.Button(self, text=stock,  fg = 'white', bg = '#6390fa', activebackground = '#30467b', font = fnt.Font(font = "Verdana 10")) #ToDo: Add command and callback.
            i += 1
            button.grid(row = i, column = 0, padx=5, pady=5)
            self.stock_buttons.append(button)

        if i == 2: # QOL notif. if no stocks.
            addstockLabel = Label(self, text = 'No stocks in profile.\n Add some on the right!', fg = 'red', bg = '#272c38', font="Verdana 10 italic")
            addstockLabel.grid(row = 3, column = 0, padx=5, pady=5)


        ### Adding a stock

        def clear_error(value): # Removes error message.
            value.destroy()

        def profile_check_callback(widget, cmd): # Handles outputting of error messages for adding a new profile and getting the input of the text box. Also handles deleting a profile to save on space.
            userInput = widget.get('1.0', 'end-1c')
            invalidInput = Label(self, text = 'Done!', fg = 'green', bg = '#1f2631', font="Verdana 10 italic")

            try:
                if cmd == add_stock: # Lazy swap between add and delete
                    cmd(profile, userInput)
                    invalidInput.grid(row = 10, column = 2)
                # else:
                #     cmd(userInput)
                #     invalidInput.grid(row = 15, column = 1)

                self.after(2000, clear_error, invalidInput)

            except ValueError as v:
                invalidInput = Label(self, text = f'{v}', fg = 'red', bg = '#1f2631', font="Verdana 10 italic") # Creates a label for the error 
                if cmd == add_stock:
                    invalidInput.grid(row = 10, column = 2)
                # else:
                #     invalidInput.grid(row = 15, column = 1)

                self.after(2000, clear_error, invalidInput) # Callback to error removal. Removes after 2 sec

        # Visual for adding stock

        newstockLabel = Label(self, text = 'Add a Stock', fg = 'white', bg = '#1f2631', font="Verdana 12")
        submitButton = tk.Button(self, text = 'Add Profile', fg = 'white', bg = '#6e819e', activebackground = '#50678a', font = fnt.Font(font = "Verdana 10"), command = lambda : profile_check_callback(newStock,add_stock)) # lambda needed so function doesn't run as soon as main is run.

        newstockLabel.grid(row = 7, column = 2)
        newStock.grid(row = 8, column = 2, padx=10, pady=10)
        submitButton.grid(row = 9, column = 2)

        '''
        To add: clicking on a individual stock will give fullname and basic markit info. Everything under backend.get_stock. 

        Combobox again in a different column for the actual selection of chart stuff along with chart settings. 
        Clicking a option in the combobox would change the options people have below it for the color/line type/etc.
        A "graph it" button would then show the charts on a new screen.

        Two back button options here, one back to the same profile and another to home page (or just back to home)


        NEED A SECTION TO ADD A STOCK AS WELL. MAYBE HAVE THE ABOVE ON A SEPERATE TAB THATS ACCESSED THROUGH A BUTTON CLICK
        ON PROFILE PAGE?


        !!!!!!! >>>>> QOL Notif for no stocks broken, persists across all screens. Maybe with the clear error?

        Have the blue banner at the top of column 1 with the name of the profile?

        '''