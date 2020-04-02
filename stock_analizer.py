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

# Skip warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

ticker = 'AAPL'  # Add company ticker for looking data
startdate = '2015-01-01'

# Get stock data from URL
data = requests.get("https://fmpcloud.io/api/v3/historical-price-full/" + ticker + "?from=" + startdate + "2&apikey=demo")
# Load the Content of the data that is in a json file
data = json.loads(data.content)
data = data['historical']  # Because it is in a dictionary, we have to look for the 'historical' content

dates = []  # List where we are going to save the dates values
close = []  # List where we are going to save the close values
adjClose = []

# ForLoop for saving the data into the lists
for item in data:
    dates.append(pd.to_datetime(item['date']))  # getting the date as a pandas time-series
    close.append(float(item['close']))  # getting the close price as a float
    adjClose.append(float(item['adjClose']))  # getting the close price as a float

# Reversing the content of the list, because we don't want the last close as our first value
close.reverse()
dates.reverse()
adjClose.reverse()

# Creating a pandas DataFrame with the values
df = pd.DataFrame(list(zip(close, adjClose)), index=dates, columns=['Close', 'adjClose'])

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

