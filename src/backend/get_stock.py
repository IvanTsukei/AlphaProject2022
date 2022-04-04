import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import numpy as np
from datetime import date

### Function Imports

import storage
from get_profile import profile_index
from get_profile import get_profile

### Misc.

df_m = pd.DataFrame()
data = storage.read_data()

### Functions

def stock_dividends(name, starting, ending):
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        for stock in existing:
            dividends = web.DataReader(stock, 'yahoo-dividends', starting, ending)
            if len(dividends) == 0:
                print(f'{stock} has no dividends for this time period.')
            else:
                print(dividends.head())
                               

def stock_basic_history(name, starting, ending):
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        for stock in existing:
            df = web.DataReader(stock, 'yahoo', start = starting, end = ending)
            if len(df) == 0:
                print(f'{stock} has no history for this time period.')
            else:
                return df.head()


### 

def portfolio_extected_return(name, starting, ending):
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        priceData = web.DataReader(existing, 'yahoo', starting, ending)
        returns = priceData['Adj Close'].pct_change()
        weights = np.full((len(existing), 1), (1/len(existing)), dtype=float)
        returns['Portfolio'] = np.dot(returns,weights)

        portfolio_annual_return = returns['Portfolio'].mean()*250
        print('Portfolio annual expected return is ' + str(np.round(portfolio_annual_return,2)*100)+'%')


def portfolio_deviation(name, starting, ending):
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        for stock in existing:
            df = web.DataReader(stock, 'yahoo', start = starting, end = ending)
            if len(df) == 0:
                print(f'{stock} has no history for this time period.')
            else:
                print(df.head())





portfolio_extected_return('A', "2015-01-01", date.today())