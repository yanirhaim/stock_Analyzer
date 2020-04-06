# Stock Analyzer
# Created by Yanir Haim

# Libraries required
import warnings
import matplotlib.pyplot as plt
import requests
import json
import pandas as pd
from indicators.rsi import rsi_status
from indicators.sma import sma_status
from indicators.bollinger_b import bollinger_b_status
from stock_data import get_stock
from indicators.rsiP import rsi_percent

# Skip warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

ticker = 'AAPL'  # Company ticker for looking data
start_date = '' # Start date of stock data, must be YY-MM-DD
end_date = '' # End date of stock data, must be YY-MM-DD

# Get the stock data as pandas dataframe
df = get_stock(ticker) # Data starting from 2015-01-01 to today's date

# df = get_stock('AAPL') # Data between days selected

# Get RSI analysis from the stock
period = 14
rsi_analysis = rsi_status(df=df, period=period)
rsi_percent = rsi_percent(df=df, period=period)

# Get the SMA analysis from the stock
ma1 = 50  # First Moving Average
ma2 = 200  # Second Moving Average
sma_analysis = sma_status(df=df, ma1=ma1, ma2=ma2)

# Get the Bollinger Bands analysis from the stock
b_period = 20
bollinger_b_status(df=df, period=b_period)

print("|------------------STOCK  TECHNICAL ANALYSIS--------------------|")
print("")
print("|------------------% RSI TECHNICAL ANALYSIS %-------------------|")
print("| RSI TREND: {}                   |".format(rsi_analysis)) 
print("| RSI PERCENTAGE: BUY: {}% | SELL: {}%                      |".format(round(rsi_percent,2), round(100 - rsi_percent,2)))
print("")
print("|------------------% SMA TECHNICAL ANALYSIS %-------------------|")
print("| SMA ANALYSIS: {}".format(sma_analysis))


# Plotting the Chart
fig = plt.figure(figsize=(14, 8))

# RSI CHART
rsi = fig.add_axes([0.1, 0.1, 0.8, 0.3])
rsi.plot(df['RSI'], label='RSI - {}'.format(period))
rsi.plot([df.index[0], df.index[-1]], [70, 70], color='red', linestyle='--')
rsi.plot([df.index[0], df.index[-1]], [30, 30], color='green', linestyle='--')
rsi.legend()

# STOCK CHART
stock = fig.add_axes([0.1, 0.4, 0.8, 0.5])
stock.plot(df['Close'], label='Close Price')
stock.plot(df['{} Daily - SMA'.format(ma1)], label='{} Daily - SMA'.format(ma1))
stock.plot(df['{} Daily - SMA'.format(ma2)], label='{} Daily - SMA'.format(ma2))
stock.set_title("{} STOCK CHART".format(ticker))
stock.legend()

plt.show()

