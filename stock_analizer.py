# Stock Analyzer
# Created by Yanir Haim

# Libraries required
import requests
import json
import pandas as pd
from indicators.rsi import rsi_status

ticker = 'AAPL'  # Add company ticker for looking data

# Get stock data from URL
data = requests.get("https://fmpcloud.io/api/v3/historical-price-full/"+ ticker +"?serietype=line&apikey=demo")
# Load the Content of the data that is in a json file
data = json.loads(data.content)
data = data['historical']  # Because it is in a dictionary, we have to look for the 'historical' content

dates = []  # List where we are going to save the dates values
close = []  # List where we are going to save the close values

# ForLoop for saving the data into the lists
for item in data:
    dates.append(pd.to_datetime(item['date']))  # getting the date as a pandas time-series
    close.append(float(item['close']))  # getting the close price as a float

# Reversing the content of the list, because we don't want the last close as our first value
close.reverse()
dates.reverse()

# Creating a pandas DataFrame with the values
df = pd.DataFrame(close, index=dates, columns=['Close'])

# Get RSI analysis from the stock
rsi_analysis = rsi_status(df=df, period=14)
print("RSI Analysis: {}".format(rsi_analysis))

