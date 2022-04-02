import storage
import yfinance as yf
from get_profile import profile_index

def add_stock(name, stock):

    # if get_profile.get_profile(profile):
    #     print (get_profile.get_profile(profile))
    #     return False
    
    def invalid_stock_input(stock):
        ticker = yf.Ticker(stock)
        if (ticker.info['regularMarketOpen'] == None):
            return "Please enter a valid stock ticker."

    if invalid_stock_input(stock):
        print(invalid_stock_input(stock))
        return False

    data = storage.read_data()

    data['profiles'][profile_index(name)].append(stock)

    storage.write_data(data)
    return True


##### WIP TO GET FUNCTION WORKING #####

