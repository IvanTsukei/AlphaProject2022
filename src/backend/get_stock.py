import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import numpy as np
from datetime import datetime

### Function Imports

import storage
from get_profile import profile_index
from get_profile import get_profile

### Misc.

df_m = pd.DataFrame()
data = storage.read_data()


'''
To Add:
- Dividend Yield
- ROE (Potentially)
- Debt to equity

Pull right from Pandas
- Market Cap
- Avg. Volume
- 1yr Target estimate
- Next earnings report date
- Beta
- Price to Earnings Ratio
- Earnings per share

'''

def stock_list(name):
    existing = data['profiles'][profile_index(name)]['stocks']
    return existing

### Functions

def stock_basic_history(name, starting, ending):
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        df = web.DataReader(existing, 'yahoo', start = starting, end = ending)
        return df.head()
        # for stock in existing:
        #     df = web.DataReader(stock, 'yahoo', start = starting, end = ending)
        #     if len(df) == 0:
        #         print(f'{stock} has no history for this time period.')
        #     else:
        #         print(df.head())


def stock_dividends(name, starting, ending):
    existing = stock_list(name)

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        for stock in existing:
            dividends = web.DataReader(stock, 'yahoo-dividends', starting, ending)
            if len(dividends) == 0:
                print(f'{stock} has no dividends for this time period.')
            else:
                print(dividends.head())


def stock_dividend_date(name):
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        divDate = web.get_quote_yahoo(existing)['dividendDate']
        print(datetime.fromtimestamp(divDate))
                            

def stock_marketcap(name):
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        marketCap = web.get_quote_yahoo(existing)['marketCap']
        print(marketCap)


def stock_pe(name):
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        priceToEarnings = web.get_quote_yahoo(existing)['trailingPE']
        print(priceToEarnings)


def stock_volume(name):
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        priceToEarnings = web.get_quote_yahoo(existing)['dailyVolume']
        print(priceToEarnings)


### Calculation Functions

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


### Misc. Helper Functions

def ticker_region(name):
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        region= web.get_quote_yahoo(existing)['region']
        print(region)


def ticker_full_name(name):
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        region= web.get_quote_yahoo(existing)['longName']
        print(region)

### Testing Below

# stock_basic_history('A', '2017-04-22', '2018-04-22')
stock_volume('A')