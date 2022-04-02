import storage
import yfinance as yf

def add_stock(prof, stock):

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

    if prof.lower() in [profile['name'].lower() for profile in data['profiles']]:
        for profile in data['profiles']:
                if profile['name'].lower() == prof.lower():
                    profile['stocks'].append(stock)

    storage.write_data(data)
    return True


##### WIP TO GET FUNCTION WORKING #####

