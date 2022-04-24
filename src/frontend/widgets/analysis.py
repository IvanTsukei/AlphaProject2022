import tkinter as tk
from tkinter import Label
from PIL import ImageTk, Image
import tkinter.font as fnt
from pathlib import Path
import pandas_datareader.data as web
import matplotlib
import numpy as np
import pandas as pd


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
    

    def analyze(self, profile):
        profile = get_profile(profile)
        profileName = profile['name'] # Needed to get the actual profile name
        self.profileName = profileName

        self.addprofileLabel = Label(self, text = f'Profile: {profileName}', fg = 'white', bg = '#242c3b', font="Verdana 11 italic")
        self.addprofileLabel.grid(row = 0, column = 3, sticky = "ne", pady=2)

