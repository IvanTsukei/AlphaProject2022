import pandas as pd
from pandas_datareader import data as pdr 
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yfin
from pandas import Series, DataFrame
from datetime import datetime

### Function Imports

import storage
from get_profile import profile_index
from get_profile import get_profile

### Misc.

yfin.pdr_override()
df_m = pd.DataFrame()
data = storage.read_data()

### Functions

def current_stock_price(name, starting, ending):
    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        for stock in existing:
            df_m[stock] = pdr.DataReader(stock, start= starting, end = ending, 
                               data_source='yahoo', interval='1mo') ['Adj Close']

def test(name, starting, ending):

    data = storage.read_data()

    existing = data['profiles'][profile_index(name)]['stocks']

    if get_profile(name) == "Please enter a valid profile name.":
        print(get_profile(name))
    else:
        # stocks = " ".join(x for x in existing)
        data = pdr.DataReader(existing, 'yahoo',starting,ending)
        data

current_stock_price('A', "2017-01-01", "2017-04-30")






