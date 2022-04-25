import pandas as pd
from datetime import timedelta, date, datetime
import pandas_datareader.data as web
import numpy as np
import yfinance as yf
from matplotlib.dates import MonthLocator, DateFormatter
import matplotlib.pyplot as plt
from pathlib import Path

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

def plot_daily_returns(data, name):
            stocks = storage.read_data()
            legend = stocks['profiles'][profile_index(name)]['stocks']
            
            fig, ax = plt.subplots(figsize=(8.260416, 2.60416), tight_layout = True)
            ax.plot(data)
            ax.legend(legend, loc='right', bbox_to_anchor=(1.114, .8), shadow=False, ncol=1, fontsize=7, frameon=False, labelcolor='white')

            ### Plotting
            ax.xaxis.set_major_locator(MonthLocator())
            ax.xaxis.set_major_formatter(DateFormatter("%b-%y"))
            ax.tick_params(axis="x", labelrotation= 30)
            ax.set_ylabel('Price ($)')

            ### Design elements
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
            ax.yaxis.label.set_color('white')
            ax.spines['bottom'].set_color('white')
            ax.spines['top'].set_color('white') 
            ax.spines['right'].set_color('white')
            ax.spines['left'].set_color('white')


            ### Saving
            fileLoc = Path(__file__).parents[1] / 'frontend' / 'widgets' /'Images' / 'dailyreturns.png'
            ax.figure.savefig(fileLoc, transparent=True)

def stock_basic_history(name):
    existing = data['profiles'][profile_index(name)]['stocks']

    today = date.today()
    yesterday = today - timedelta(days = 360)

    df = web.DataReader(existing, 'yahoo',yesterday, today)['Adj Close']
    df = df.clip(lower = 0) # Since my stock adder isn't perfect, tickers like SNSLF can get in which break it.

    plot_daily_returns(df, name)


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
            try:
                beta = info['beta']
            except KeyError: # Def. not the right way to do this but no time to fix. Calc. will be wrong but crash avoided.
                beta = 1
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
    weeknumber = datetime.today().weekday()

    ## Will still break for holidays where the market is closed during a weekday.
    if weeknumber == 5:
        yesterday = today - timedelta(days = 1)
        df = web.DataReader(ticker, 'yahoo',yesterday, today)
    elif weeknumber == 6:
        yesterday = today - timedelta(days = 2)
        df = web.DataReader(ticker, 'yahoo',yesterday, today)
    else:
        df = web.DataReader(ticker, 'yahoo', today)


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
        df['divAmount'] = float(web.get_quote_yahoo(ticker)['trailingAnnualDividendYield'])
    except KeyError:
        df['divAmount'] = ('-NA-')

    try:
        df['analystRating'] = str(web.get_quote_yahoo(ticker)['averageAnalystRating'])
    except KeyError:
        df['analystRating'] = ('-NA-')

    df.drop(['Low', 'Adj Close'], axis=1, inplace=True)

    return df