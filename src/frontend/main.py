import tkinter as tk
import matplotlib

#Widgets, to-do, different screens.
from frontend.widgets.stock import StockWidget
from frontend.widgets.profiles import ProfilesWidget
from frontend.widgets.profile import ProfileWidget



class App(tk.Tk):
    state = "Home"

    def __init__(self):
        super().__init__()
        self.title("Cool Stock Project")
        self.configure(bg='white')
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))

        self.plistWidget = ProfilesWidget(self, self.select_profile_callback)
        self.plistWidget.grid(row = 0, column = 0, sticky = "ew") #show it.

        self.pWidget = ProfileWidget(self, self.back_callback)

    def clear_screen(self):
        self.plistWidget.grid_remove()
        self.pWidget.grid_remove()

    def back_callback(self):
        self.clear_screen()
        if self.state == "Profile":
            self.state == "Home"
            self.plistWidget.grid(row = 0, column = 0, sticky = "ew")

    def select_profile_callback(self, profile):
        self.clear_screen()
        self.pWidget.show(profile)
        self.pWidget.grid(row = 0, column = 0, sticky = "ew")
        self.state = "Profile"






