import backend.storage as storage
import yfinance as yf
from backend.get_profile import profile_index
from backend.get_profile import get_profile

### Main

def delete_stock(name, stock):

    data = storage.read_data()

    ### Checking if stock ticker is valid.

    def stock_exists(stock):
        existing = data['profiles'][profile_index(name)]['stocks']
        if stock not in existing:
            raise ValueError ("This Ticker is not in the Profile.")


    ### Adding the stock after checking if the profile exists.

    # if get_profile(name) == "Please enter a valid profile name.":
    #     print(get_profile(name))

    if stock_exists(stock):
        print(stock_exists(stock))
        return False

    else:
        data['profiles'][profile_index(name)]['stocks'].remove(stock)

    storage.write_data(data)
    return True
