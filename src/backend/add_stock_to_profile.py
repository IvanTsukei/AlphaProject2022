import backend.storage as storage
import pandas_datareader.data as web
from backend.get_profile import profile_index

### Main

def add_stock(name, stock):

    data = storage.read_data()

    ### Checking if stock ticker is valid.
    
    def invalid_stock_input(stock):

        # If no entry
        if stock == "":
            raise ValueError ("Not a valid stock ticker.")

        # Checks if a bid exists. Good indicator of if the stock is valid
        try:
            int(web.get_quote_yahoo(stock)['bid'])
        except (KeyError, IndexError):
            raise ValueError ("Not a valid stock ticker.")

    def stock_exists(stock):
        existing = data['profiles'][profile_index(name)]['stocks']
        if stock.upper() in existing:
            raise ValueError ("This Ticker is already in this profile.")

    if invalid_stock_input(stock):
        print(invalid_stock_input(stock))
        return False

    if stock_exists(stock):
        print(stock_exists(stock))
        return False

    else:
        data['profiles'][profile_index(name)]['stocks'].append(stock.upper())

    storage.write_data(data)
    return True