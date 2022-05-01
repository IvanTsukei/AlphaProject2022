import backend.storage as storage
from backend.get_profile import profile_index
from backend.get_profile import get_profile

### Main

def delete_stock(name, stock):
    """
    Function for deleting a stock from the profile.
    """

    data = storage.read_data()

    def stock_exists(stock):
        """
        Checks if the stock is actually in the profile.
        """
        existing = data['profiles'][profile_index(name)]['stocks']
        if stock.upper() not in existing:
            raise ValueError ("This Ticker is not in the Profile.")

    if stock_exists(stock):
        print(stock_exists(stock))
        return False

    else:
        data['profiles'][profile_index(name)]['stocks'].remove(stock.upper())

    storage.write_data(data)
    return True
