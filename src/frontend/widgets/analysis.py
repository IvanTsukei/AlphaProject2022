import tkinter as tk
from tkinter import Label
from PIL import ImageTk, Image
import tkinter.font as fnt
from pathlib import Path
import pandas_datareader.data as web
import matplotlib
import numpy as np
import pandas as pd

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
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


        def plot_daily_returns():
            stocks = storage.read_data()
            data = stock_basic_history(profileName)
            legend = stocks['profiles'][profile_index(profileName)]['stocks']

            fig = Figure(figsize=(6, 4), tight_layout = True)
            plot1 = fig.add_subplot(111)
            fig.subplots_adjust(wspace=0, hspace=0)
            plot1.plot(data)
            plot1.legend(legend, loc='right', bbox_to_anchor=(1.25, .8), shadow=False, ncol=1)


            plot1.xaxis.set_major_locator(MonthLocator())
            plot1.xaxis.set_major_formatter(DateFormatter("%b-%y"))
            plot1.tick_params(axis="x", labelrotation= 30)
            plot1.set_ylabel('1 Year Returns')
            plot1.set_ylabel('Price ($)')



            canvas = FigureCanvasTkAgg(fig, master = self)  
            # canvas.get_tk_widget().grid(row = 0, column = 0)
            canvas.draw()
            fileLoc = Path(__file__).parent.resolve() / 'Images' / 'dailyreturns.png'
            plt.savefig(fileLoc)


        def show_returns():
            fileLoc = Path(__file__).parent.resolve() / 'Images' / 'dailyreturns.png'
            plt.savefig(fileLoc)


        plot_daily_returns()

