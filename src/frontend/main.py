import tkinter as tk
import matplotlib

#Widgets, to-do, different screens.
from frontend.widgets.stock import StockWidget


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cool Stock Project")
        self.configure(bg='white')
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))

        #Testing
        self.stockWidget = StockWidget(self, "MSFT")
        self.stockWidget.grid(row = 0, column = 0, sticky="ew")


