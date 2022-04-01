import storage
import yfinance as yf
import get_profile

def add_stock(profile, stock):

    # if get_profile.get_profile(profile):
    #     print (get_profile.get_profile(profile))
    #     return False

    currentProfiles = storage.read_data()['profiles']
    
    def invalid_stock_input(stock):
        ticker = yf.Ticker(stock)
        if (ticker.info['regularMarketOpen'] == None):
            return "Please enter a valid stock ticker."

    if invalid_stock_input(stock):
        print(invalid_stock_input(stock))
        return False


    data = storage.read_data()
    print(get_profile.get_profile(profile)['stocks'])
    print(stock)
    data[get_profile.get_profile(profile)]['stocks'].append(stock)
    print(get_profile.get_profile(profile)['stocks'])
    storage.write_data(data)
    return True


##### WIP TO GET FUNCTION WORKING #####

add_stock('R','MSFT')