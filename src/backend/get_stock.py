import pandas as pd
from datetime import timedelta, date
import pandas_datareader.data as web
import numpy as np
import yfinance as yf

### Function Imports

import backend.storage as storage
from backend.get_profile import profile_index
from backend.get_profile import get_profile

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
        df = web.DataReader(existing, 'yahoo', starting, ending)
        return df.head()


def portfolio_dividends(name, starting, ending):
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
                            

def portfolio_daily_returns(name, starting, ending): # % change
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        returns_data = web.DataReader(existing, 'yahoo', starting, ending)['Adj Close']
        returns = returns_data.pct_change()
        returns.dropna(inplace = True)
        return returns


def portfolio_beta(name):
    existing = data['profiles'][profile_index(name)]['stocks']

    weights = [1/len(existing) for x in range(len(existing))] # Don't have time to code a more complex system that would allow people to enter their own weights. This assumes equally weighted portfolio 

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        raw_beta = []
        weighted_beta = []

        for stock in existing: 
            info = yf.Ticker(stock).info
            beta = info['beta']
            raw_beta.append(beta)
        
        for x, y in zip(weights, raw_beta): # Accounting for the weight of each stock on the portfolio
            weighted_beta.append(x*y)

        res = (sum(weighted_beta))
        return (f'{res:.4f}')

### Calculation Functions

def portfolio_extected_return(name, starting, ending):
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        price_data = web.DataReader(existing, 'yahoo', starting, ending)
        returns = price_data['Adj Close'].pct_change()
        weights = np.full((len(existing), 1), (1/len(existing)), dtype=float)
        returns['Portfolio'] = np.dot(returns,weights)

        portfolio_annual_return = returns['Portfolio'].mean()*250
        print('Portfolio annual expected return is ' + str(np.round(portfolio_annual_return,2)*100)+'%')

###################################################################

def all_basic_stock_info(ticker):

    today = date.today()
    yesterday = today - timedelta(days = 180) # In case this is run between 12am and 9:30am of the following day

    df = web.DataReader(ticker, 'yahoo',yesterday, today)

    try:
        df['fiftyTwoHigh'] = float(web.get_quote_yahoo(ticker)['fiftyTwoWeekHigh'])
    except KeyError:
        df['fiftyTwoHigh'] = ('-NA-')
    
    try:
        df['longName'] = str(web.get_quote_yahoo(ticker)['longName'])
    except KeyError:
        df['longName'] = ('-NA-')
    
    try:
        df['trailingPE'] = float(web.get_quote_yahoo(ticker)['trailingPE'])
    except KeyError:
        df['trailingPE'] = ('-NA-')
    
    try:
        df['marketCap'] = int(web.get_quote_yahoo(ticker)['marketCap'])
    except KeyError:
        df['marketCap'] =  ('-NA-')

    try:
        df['divAmount'] = web.DataReader('IBM', 'yahoo-dividends', yesterday, today).iat[1,1]
    except KeyError:
        df['divAmount'] = ('-NA-')

    df.drop(['Low', 'Adj Close'], axis=1, inplace=True)

    return df