import pandas as pd
import yfinance as yf
import numpy as np
import storage
# import pyqt5 as pyq

print(storage.read_data())


print('> Welcome to the Stock notifier!\nPlease input the ticker symbols for the stocks you wish to look up.')

def rawData():
    uinput_tickers = input()
    tickers = list([map(lambda t: yf.Ticker(t), uinput_tickers.split(" "))][0])
    print (tickers)

    # while True:
    #     print(f'Your current stock selection is: {tickers}')
    #     print(tickers)
        # selection = input('> Which of your stocks would you like to see more information about? Use numbers, starting at 1, to make your selection:\n ')
        # data_options = input('> Select the information type you\'d like to see, or type q to quit.\nValid searches are: info, dividends, splits, options, recommendations, earnings, actions, news.\n')
        # one_ticker = list(tickers)[selection] + 1

        # if data_options == 'info' or data_options == 'Info':
        #     print(f'tickers.tickers.{one_ticker}.info')
        # elif data_options == 'info' or data_options == 'Info':
        #     print(f'tickers.tickers.{one_ticker}.info')
        # elif data_options == 'q' or data_options == 'Q':
        #     break
        # else:
        #     continuethi

rawData()


