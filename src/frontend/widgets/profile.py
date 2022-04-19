import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.messagebox import showerror
import tkinter.font as fnt
from pathlib import Path

from backend.get_profile import get_profile
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

        print(profile)

        i = 2
        for stock in profile['stocks']:
            button = tk.Button(self, text=stock,  fg = 'white', bg = '#6390fa', activebackground = '#30467b', font = fnt.Font(font = "Verdana 10")) #ToDo: Add command and callback.
            i += 1
            button.grid(row = i, column = 0, padx=5, pady=5)
            self.stock_buttons.append(button)

        if i == 2: # QOL notif. if no stocks.
            addstockLabel = Label(self, text = 'No stocks in profile.\n Add some on the right!', fg = 'red', bg = '#272c38', font="Verdana 10 italic")
            addstockLabel.grid(row = 3, column = 0, padx=5, pady=5)

        '''
        To add: clicking on a individual stock will give fullname and basic markit info. Everything under backend.get_stock. 

        Combobox again in a different column for the actual selection of chart stuff along with chart settings. 
        Clicking a option in the combobox would change the options people have below it for the color/line type/etc.
        A "graph it" button would then show the charts on a new screen.

        Two back button options here, one back to the same profile and another to home page (or just back to home)


        NEED A SECTION TO ADD A STOCK AS WELL. MAYBE HAVE THE ABOVE ON A SEPERATE TAB THATS ACCESSED THROUGH A BUTTON CLICK
        ON PROFILE PAGE?


        QOL Notif for no stocks broken, persists across all screens. Maybe with the clear error?

        '''