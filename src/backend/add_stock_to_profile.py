import backend.storage as storage
import yfinance as yf
from backend.get_profile import profile_index
from backend.get_profile import get_profile

def add_stock(name, stock):

    data = storage.read_data()

    ### Checking if stock ticker is valid.
    
    def invalid_stock_input(stock):
        ticker = yf.Ticker(stock)
        if (ticker.info['regularMarketOpen'] == None):
            return "Please enter a valid stock ticker."

    def stock_exists(stock):
        existing = data['profiles'][profile_index(name)]['stocks']
        if stock in existing:
            return "This Ticker is already in this profile."

    if invalid_stock_input(stock):
        print(invalid_stock_input(stock))
        return False

    ### Adding the stock after checking if the profile exists.

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))

    elif stock_exists(stock):
        print(stock_exists(stock))
        return False

    else:
        data['profiles'][profile_index(name)]['stocks'].append(stock)

    storage.write_data(data)
    return True
