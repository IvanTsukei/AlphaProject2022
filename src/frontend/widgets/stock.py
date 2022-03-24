import tkinter as tk


class StockWidget(tk.Frame):
    def __init__(self, parent, stock_ticker):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.label = tk.Label(self, text = stock_ticker)
        self.label.grid(row = 0, column = 0)

