import tkinter as tk
from tkinter import Label
from PIL import ImageTk, Image
import tkinter.font as fnt
from pathlib import Path
import pandas_datareader.data as web

from backend.get_profile import get_profile
from backend.add_stock_to_profile import add_stock
from backend.delete_stock_from_profile import delete_stock
from backend.get_stock import all_basic_stock_info

### Main

class ProfileWidget(tk.Frame):
    def __init__(self, parent, back_callback):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.back_button = tk.Button(self, text="Back", fg = 'white', bg = '#6e819e', activebackground = '#f4595d', activeforeground = '#2a2b2c', font = fnt.Font(font = "Verdana 10 bold"), command = back_callback)
        self.reload_button = tk.Button(self, text="Reload", fg = 'white', bg = '#6e819e', activebackground = '#6390fa', activeforeground = '#2a2b2c', font = fnt.Font(font = "Verdana 10 bold"), command = self.reload)
        self.back_button.grid(row = 0, column = 0, sticky = "nw")
        self.reload_button.grid(row = 0, column = 0, sticky = "e")


        ### Design Elements

        self.configure(bg='#272c38')
        self.grid_columnconfigure(0, minsize=133)
        self.grid_columnconfigure(1, minsize=200)
        self.grid_columnconfigure(2, minsize=220)
        self.grid_columnconfigure(3, minsize=347)
        self.grid_rowconfigure(15, minsize=698) # Extend widget to full canvas size
        self.grid_rowconfigure(2, minsize=115) # To move stock list down

        self.stock_buttons = []

    ### Main Stuff Below

    def reload(self):
        self.show(self.profileName)


    def show(self, profile_name):
        profile = get_profile(profile_name)
        profileName = profile['name'] # Needed to get the actual profile name
        self.profileName = profileName

        ### CLEARING OUT OLD INFO

        if (hasattr(self, 'addstockLabel')): # Clears the empty list label
            self.addstockLabel.destroy()
        
        if (hasattr(self, 'addprofileLabel')): # Clears the empty list label
            self.addprofileLabel.destroy()


        ### Can't figure out out to get to the labels within the function, global isn't working, so this awful workaround will have to do for now.
        def clear_basic_info(self):

            ### Clearing Previous Info

            allLabels = ['self.one', 'self.two', 'self.three', 'self.four', 'self.five', 'self.six', 'self.seven', 'self.eight', 'self.nine', 'self.ten']

            for i in allLabels: # Saving space
                if (hasattr(self, i)): # Clears the empty list label
                    self.i.destroy()
                
            ### Function Values

            ### The Labels

            text_empty = '                            '
            self.one    = Label(self, text = text_empty, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.two    = Label(self, text = text_empty, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.three  = Label(self, text = text_empty, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.four   = Label(self, text = text_empty, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.five   = Label(self, text = text_empty, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.six    = Label(self, text = text_empty, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.seven  = Label(self, text = text_empty, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.eight  = Label(self, text = text_empty, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.nine   = Label(self, text = text_empty, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.ten    = Label(self, text = text_empty, fg = 'white', bg = '#1f2631', font="Verdana 11")

            ### Plotting the labels

            self.one.grid(row = 5, column = 1, padx=5, pady=5, sticky = 'w')
            self.two.grid(row = 6, column = 1, padx=5, pady=5, sticky = 'w')
            self.three.grid(row = 7, column = 1, padx=5, pady=5, sticky = 'w')
            self.four.grid(row = 8, column = 1, padx=5, pady=5, sticky = 'w')
            self.five.grid(row = 9, column = 1, padx=5, pady=5, sticky = 'w')
            self.six.grid(row = 10, column = 1, padx=5, pady=5, sticky = 'w')
            self.seven.grid(row = 11, column = 1, padx=5, pady=5, sticky = 'w')
            self.eight.grid(row = 12, column = 1, padx=5, pady=5, sticky = 'w')
            self.nine.grid(row = 13, column = 1, padx=5, pady=5, sticky = 'w')
            self.ten.grid(row = 14, column = 1, padx=5, pady=5, sticky = 'w')
        
        clear_basic_info(self)

        ### Showing Profile Name in Top Right

        self.addprofileLabel = Label(self, text = f'Profile: {profileName}', fg = 'white', bg = '#242c3b', font="Verdana 11 italic")
        self.addprofileLabel.grid(row = 0, column = 3, sticky = "ne", pady=2)

        ### Entry Methods

        newStock = tk.Text(self, height = 1, width = 22, padx=10, pady=10, foreground="#2a2b2c", bg='#628ffa', font="Verdana 12 bold", borderwidth=2) # Initiating the stock adding textbox
        deleteStock = tk.Text(self, height = 1, width = 22, padx=10, pady=10, foreground="#2a2b2c", bg='#628ffa', font="Verdana 12 bold", borderwidth=2) # Initiating the stock deleting textbox
        graphButton = tk.Button(self, text = 'Start Portfolio Analysis', fg = 'white', bg = '#6e819e', activebackground = '#50678a', font = fnt.Font(font = "Verdana 10"))
        

        ### BG Image

        bgImage = Path(__file__).parent.resolve() / 'Images' / 'ProfileBG.png'

        homeBGLoc = Image.open(bgImage)
        homeBG = ImageTk.PhotoImage(homeBGLoc)

        homeBGDiv = tk.Label(self, image = homeBG)
        homeBGDiv.image = homeBG
        homeBGDiv.place(x=0, y=0, relwidth=1)
        homeBGDiv.lower()


        ### Diving Line Widgets

        maindivImage = Path(__file__).parent.resolve() / 'Images' / 'MiscPinkDiv.png'

        topdivlineLoc = Image.open(maindivImage)
        topdivLine = ImageTk.PhotoImage(topdivlineLoc)

        topplacedDiv = tk.Label(self, image = topdivLine, bg = '#1f2631')
        topplacedDiv.image = topdivLine # Saving the ref
        topplacedDiv.place(x = 610, y = 424)

        ### Adding all stocks in profile

        def easy_read_format(value):
            if value == "-NA-":
                return "-NA-"
            num = float('{:.3g}'.format(value))
            size = 0
            while abs(num) >= 1000:
                size += 1
                num /= 1000.0
            return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][size])

        ## Individual stock info
        def stocks_basic_info(self, stock):

            ### Clearing Previous Info

            allLabels = ['self.markepcapLabel', 'self.peLabel', 'self.fiftytwoHighLabel', 'self.volumeLabel', 'self.highLabel', 'self.fullnameLabel', 'self.divRateLabel', 'self.priceLabel', 'self.closeLabel', 'self.analystLabel']

            for i in allLabels: # Saving space
                if (hasattr(self, i)): # Clears the empty list label
                    i.destroy()
                
            ### Function Values

            df = all_basic_stock_info(stock) # SO much faster than using yfinance and doing a query on each key

            print(df)
            
            marketCap = easy_read_format(df.iat[0,7])
            volume = easy_read_format(df.iat[0,3])
            firstfullName = df.iat[0,5]

            if df.iat[0,6] == "-NA-":
                pe = "-NA-"
            else:
                pe = f'{df.iat[0,6]:.3f}'

            
            if df.iat[0,0] == "-NA-":
                high = "-NA-"
            else:
                high = f'${df.iat[0,0]:.2f}'

            if df.iat[0,1] == "-NA-":
                close = "-NA-"
            else:
                close = f'${df.iat[0,1]:.2f}'

            
            if df.iat[0,4] == "-NA-":
                fiftytwoHigh = "-NA-"
            else:
                fiftytwoHigh = f'${df.iat[0,4]:.2f}'

            
            if df.iat[0,8] == "-NA-":
                divRate = "-NA-"
            else:
                divRate = f'{df.iat[0,8]:,.2%}'

            
            if df.iat[0,1] == "-NA-":
                price = "-NA-"
            else:
                price = f'${df.iat[0,1]:.2f}'

            if df.iat[0,9] == "-NA-":
                analysts = "-NA-"
            else:
                analysts = df.iat[0,9]
                analystsFirst = analysts.split('\n')[0]
                analystsRes1 = "".join(str(x) for x in analystsFirst)
                analystFinal = analystsRes1.split('    ')[1]
    
            print(analystFinal)
            firstfullName = firstfullName.split('\n')[0]
            nextfullName = "".join(str(x) for x in firstfullName)
            fullName = nextfullName.split('    ')[1]

            self.markepcapLabel     = Label(self, text = f'${marketCap}', fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.peLabel            = Label(self, text = pe, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.fiftytwoHighLabel  = Label(self, text = fiftytwoHigh, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.volumeLabel        = Label(self, text = volume, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.highLabel          = Label(self, text = high, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.fullnameLabel      = Label(self, text = f'{fullName[:13]}...', fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.divRateLabel       = Label(self, text = divRate, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.priceLabel         = Label(self, text = price, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.closeLabel         = Label(self, text = close, fg = 'white', bg = '#1f2631', font="Verdana 11")
            self.analystLabel       = Label(self, text = analystFinal, fg = 'white', bg = '#1f2631', font="Verdana 11")

            ### Plotting the labels

            self.fullnameLabel.grid(row = 5, column = 1, padx=5, pady=5, sticky = 'w')
            self.priceLabel.grid(row = 6, column = 1, padx=5, pady=5, sticky = 'w')
            self.highLabel.grid(row = 7, column = 1, padx=5, pady=5, sticky = 'w')
            self.closeLabel.grid(row = 8, column = 1, padx=5, pady=5, sticky = 'w')
            self.fiftytwoHighLabel.grid(row = 9, column = 1, padx=5, pady=5, sticky = 'w')
            self.markepcapLabel.grid(row = 10, column = 1, padx=5, pady=5, sticky = 'w')
            self.volumeLabel.grid(row = 11, column = 1, padx=5, pady=5, sticky = 'w')
            self.peLabel.grid(row = 12, column = 1, padx=5, pady=5, sticky = 'w')
            self.divRateLabel.grid(row = 13, column = 1, padx=5, pady=5, sticky = 'w')
            self.analystLabel.grid(row = 14, column = 1, padx=5, pady=5, sticky = 'w')

        
        ### Individual Stocks

        for button in self.stock_buttons:
            button.destroy()
        self.stock_buttons = []

        i = 4
        for stock in profile['stocks']:
            button = tk.Button(self, text=stock,  fg = 'white', bg = '#6390fa', activebackground = '#30467b', font = fnt.Font(font = "Verdana 10"), command=lambda stock=stock:stocks_basic_info(self, stock)) # FINALLY got the button click to register the ticker name...
            i += 1 # Next row
            button.grid(row = i, column = 2, padx=5, pady=5)
            self.stock_buttons.append(button)

        if i == 4: # QOL notif. if no stocks.
            self.addstockLabel = Label(self, text = 'No stocks in profile.\n Add some on the right!', fg = 'red', bg = '#1f2631', font="Verdana 10 italic")
            self.addstockLabel.grid(row = 5, column = 2, padx=5, pady=5)


        ### Adding a new stock to profile

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
                    invalidInput.place(x = 711, y = 401)

                self.after(2000, clear_error, invalidInput)

            except ValueError as v:
                invalidInput = Label(self, text = f'{v}', fg = 'red', bg = '#1f2631', font="Verdana 10 italic") # Creates a label for the error 
                if cmd == add_stock:
                    invalidInput.place(x = 618, y = 226)
                else:
                    invalidInput.place(x = 618, y = 401)

                self.after(2000, clear_error, invalidInput) # Callback to error removal. Removes after 2 sec

        # Visual for adding stock

        newstockLabel = Label(self, text = 'Add a Stock', fg = 'white', bg = '#1f2631', font="Verdana 12")
        submitButton = tk.Button(self, text = 'Add Stock', fg = 'white', bg = '#6e819e', activebackground = '#59f4b4', activeforeground = '#2a2b2c', font = fnt.Font(font = "Verdana 10"), command = lambda : profile_check_callback(newStock,add_stock)) # lambda needed so function doesn't run as soon as main is run.


        newStock.place(x = 598, y = 137) #### using place since the auto resize of rows makes it a mess
        submitButton.place(x = 693, y = 189)

        ### Deleting a stock

        deletestockLabel = Label(self, text = 'Delete a Stock', fg = 'white', bg = '#1f2631', font="Verdana 12")
        submitdeleteButton = tk.Button(self, text = 'Delete Stock', fg = 'white', bg = '#6e819e', activebackground = '#f4595d', activeforeground = '#2a2b2c', font = fnt.Font(font = "Verdana 10"), command = lambda : profile_check_callback(deleteStock,delete_stock)) # lambda needed so function doesn't run as soon as main is run.
        

        deleteStock.place(x = 598, y = 312)
        submitdeleteButton.place(x = 683, y = 364)

        graphButton.place(x = 651, y = 462)


        ### Portfolio Beta


        # portbeta = portfolio_beta(profileName)


        # portbetaLabel = Label(self, text = f'{portbeta}', fg = 'white', bg = '#1f2631', font="Verdana 12")

        # portbetaLabel.place(x = 651, y = 562)
        
        
        '''
        To add: clicking on a individual stock will give fullname and basic markit info. Everything under backend.get_stock. 

        Combobox again in a different column for the actual selection of chart stuff along with chart settings. 
        Clicking a option in the combobox would change the options people have below it for the color/line type/etc.
        A "graph it" button would then show the charts on a new screen.

        Two back button options here, one back to the same profile and another to home page (or just back to home)


        Limit # of stock inputs

        '''
