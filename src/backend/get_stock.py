import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import numpy as np
from datetime import date
from scipy import stats
import seaborn as sns
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

def easy_read_format(value):
    num = float('{:.3g}'.format(value))
    size = 0
    while abs(num) >= 1000:
        size += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][size])

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


def stock_dividend_date(name): # Broken, needs fixing
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        div_date = web.get_quote_yahoo(existing)['dividendDate']
        print(div_date)
                            

def stock_marketcap(stock):
    # existing = data['profiles'][profile_index(name)]['stocks']

    # if get_profile(name) == "Please enter a valid profile name.":
    #     print(get_profile(name))
    # else:
    # market_cap = web.get_quote_yahoo(stock)['marketCap']
    # return market_cap
    info = yf.Ticker(stock).info
    market_cap = info['marketCap']

    return (f'${easy_read_format(market_cap)}')


def stock_pe(stock):
    # existing = data['profiles'][profile_index(name)]['stocks']

    # if get_profile(name) == "Please enter a valid profile name.":
    #     print(get_profile(name))
    # else:
    # price_earnings = web.get_quote_yahoo(stock)['trailingPE']
    # return price_earnings
    info = yf.Ticker(stock).info
    price_earnings = info['trailingPE']
    return (f'{price_earnings:.3f}')


def portfolio_daily_returns(name, starting, ending): # % change
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        returns_data = web.DataReader(existing, 'yahoo', starting, ending)['Adj Close']
        returns = returns_data.pct_change()
        returns.dropna(inplace = True)
        return returns


def stock_industry(stock):
    # existing = data['profiles'][profile_index(name)]['stocks']

    # if get_profile(name) == "Please enter a valid profile name.":
    #     print(get_profile(name))
    # else:
    #     df = pd.DataFrame()

        # for stock in existing:
    info = yf.Ticker(stock).info
    industry = info['industry']
            # df = df.append({'Industry':industry}, ignore_index=True)

    return industry

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

        return (sum(weighted_beta))


def stock_volume(stock):
    # existing = data['profiles'][profile_index(name)]['stocks']
    

    # if get_profile(name) == "Please enter a valid profile name.":
    #     print(get_profile(name))
    # else:
    info = yf.Ticker(stock).info
    volume = info['averageVolume']
    return easy_read_format(volume)


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


### Misc. Helper Functions

def ticker_high(stock):
    # existing = data['profiles'][profile_index(name)]['stocks']

    # if get_profile(name) == "Please enter a valid profile name.":
    #     print(get_profile(name))
    # else:
    info = yf.Ticker(stock).info
    high = info['fiftyTwoWeekHigh']
    return (f'${high}')

def ticker_price(stock):
    # existing = data['profiles'][profile_index(name)]['stocks']

    # if get_profile(name) == "Please enter a valid profile name.":
    #     print(get_profile(name))
    # else:
    info = yf.Ticker(stock).info
    price = info['regularMarketPrice']
    return (f'${price}')
    


def ticker_full_name(stock):
    # existing = data['profiles'][profile_index(name)]['stocks']

    # if get_profile(name) == "Please enter a valid profile name.":
    #     print(get_profile(name))
    # else:
    # fullname = web.get_quote_yahoo(stock)['longName']
    # return fullname
    info = yf.Ticker(stock).info
    fullname = info['longName']
    return fullname[:15]

def dividend_rate(stock):
    # existing = data['profiles'][profile_index(name)]['stocks']

    # if get_profile(name) == "Please enter a valid profile name.":
    #     print(get_profile(name))
    # else:
    # fullname = web.get_quote_yahoo(stock)['longName']
    # return fullname
    info = yf.Ticker(stock).info
    dividendRate = info['dividendRate']
    if dividendRate != None:
        return dividendRate
    else:
        return "-NA-"

### Testing Below


