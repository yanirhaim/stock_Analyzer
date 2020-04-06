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

# Skip warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

ticker = 'AAPL'  # Company ticker for looking data
startdate = '2015-01-01'  # Start-date of the stock data YY/MM/DD

df = get_stock('AAPL')

# Get RSI analysis from the stock
period = 14
rsi_analysis = rsi_status(df=df, period=period)

# Get the SMA analysis from the stock
ma1 = 50  # First Moving Average
ma2 = 200  # Second Moving Average
sma_analysis = sma_status(df=df, ma1=ma1, ma2=ma2)

# Get the Bollinger Bands analysis from the stock
b_period = 20
bollinger_b_status(df=df, period=b_period)

print("<------------------STOCK  TECHNICAL ANALYSIS-------------------->")
print("RSI ANALYSIS: {}".format(rsi_analysis))
print("SMA ANALYSIS: {}".format(sma_analysis))
print(df['adjClose'])

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

