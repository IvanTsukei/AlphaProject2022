import tkinter as tk
import matplotlib

from tkinter import *
from tkinter import ttk

#Widgets, to-do, different screens.
from frontend.widgets.stock import StockWidget
from frontend.widgets.profiles import ProfilesWidget
from frontend.widgets.profile import ProfileWidget
from frontend.widgets.analysis import AnalysisWidget

### Main

class App(tk.Tk):
    state = "Home"

    def __init__(self):
        super().__init__()
        self.title("Python Portfolio Tracker")
        self.configure(bg='#272c38')
        # w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        # self.geometry("%dx%d+0+0" % (w, h))  # Fullscreen
        self.geometry("900x900")
        self.resizable(False, False) # Disables resizing

        self.plistWidget = ProfilesWidget(self, self.select_profile_callback)
        self.plistWidget.grid(rowspan = 16, column = 1) # Show it

        self.pWidget = ProfileWidget(self, self.back_callback, self.start_portfolio_analysis_callback)

        self.analysisWidget = AnalysisWidget(self, self.back_callback)

    def clear_screen(self):
        self.plistWidget.grid_remove()
        self.pWidget.grid_remove()
        self.analysisWidget.grid_remove()

    def back_callback(self):
        self.clear_screen()
        if self.state == "Profile":
            self.state == "Home"
            self.plistWidget.grid(row = 0, column = 0, sticky = "ew")
        elif self.state == "Analysis":
            self.state == "Home"
            self.plistWidget.grid(row = 0, column = 0, sticky = "ew")

    def select_profile_callback(self, profile):
        self.clear_screen()
        self.pWidget.show(profile)
        self.pWidget.grid(row = 0, column = 0, sticky = "ew")
        self.state = "Profile"

    def start_portfolio_analysis_callback(self, profile):
        self.clear_screen()
        self.analysisWidget.analyze(profile)
        self.analysisWidget.grid(row = 0, column = 0, sticky = "ew")
        self.state = "Analysis"
