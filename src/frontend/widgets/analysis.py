import tkinter as tk
from tkinter import Label
from PIL import ImageTk, Image
import tkinter.font as fnt
from pathlib import Path
import pandas_datareader.data as web
import pandas as pd
import time


from matplotlib.dates import MonthLocator, DateFormatter
import matplotlib.pyplot as plt


from backend.get_stock import stock_basic_history
from backend.get_profile import get_profile, profile_index
import backend.storage as storage

class AnalysisWidget(tk.Frame):
    def __init__(self, parent, back_callback):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.back_button = tk.Button(self, text="Back", fg = 'white', bg = '#6e819e', activebackground = '#f4595d', activeforeground = '#2a2b2c', font = fnt.Font(font = "Verdana 10 bold"), command = back_callback)
        self.back_button.grid(row = 0, column = 0, sticky = "nw")

        self.configure(bg='#272c38')
        self.grid_rowconfigure(15, minsize=900) # Extend widget to full canvas size
        self.grid_columnconfigure(0, minsize=133)
        self.grid_columnconfigure(1, minsize=200)
        self.grid_columnconfigure(2, minsize=220)
        self.grid_columnconfigure(3, minsize=347)

        ### BG Image

        bgImage = Path(__file__).parent.resolve() / 'Images' / 'AnalysisPage.png'

        homeBGLoc = Image.open(bgImage)
        homeBG = ImageTk.PhotoImage(homeBGLoc)

        homeBGDiv = tk.Label(self, image = homeBG)
        homeBGDiv.image = homeBG
        homeBGDiv.place(x=0, y=0, relwidth=1)
        homeBGDiv.lower()
    

    def analyze(self, profile):
        profile = get_profile(profile)
        profileName = profile['name'] # Needed to get the actual profile name
        self.profileName = profileName

        self.addprofileLabel = Label(self, text = f'Profile: {profileName}', fg = 'white', bg = '#242c3b', font="Verdana 11 italic")
        self.addprofileLabel.grid(row = 0, column = 3, sticky = "ne", pady=2)

        def show_returns():
            # invalidInput = Label(self, text = 'Generating Graph...', fg = 'green', bg = '#232833', font="Verdana 8 italic")
            # invalidInput.place(x = 393, y = 583)
            # self.after(2000, clear_error, invalidInput)

            stock_basic_history(profileName)

            time.sleep(2) # Give the pc a second to update the file

            returnsGraph = Path(__file__).parent.resolve() / 'Images' / 'dailyreturns.png'

            self.graphbgImageLoc = Image.open(returnsGraph)
            self.graphbgImage = ImageTk.PhotoImage(self.graphbgImageLoc)
            self.graphbgImageDiv = tk.Label(self, image = self.graphbgImage, bg = '#1f2631')
            self.graphbgImageDiv.image = self.graphbgImage # Saving the ref
            self.graphbgImageDiv.place(x = 34, y = 590)


        self.plot_button = tk.Button(self, text="Plot 1yr Returns", fg = 'white', bg = '#6e819e', activebackground = '#6390fa', activeforeground = '#2a2b2c', font = fnt.Font(font = "Verdana 10 bold"), command = show_returns)
        self.plot_button.place(x = 390, y = 555)


