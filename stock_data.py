import datetime as datetime
import requests
import json
import pandas as pd

current_d = datetime.datetime.today().strftime('%Y-%m-%d')

def get_stock(ticker, start_date='2015-01-01', end_date=current_d):
	data = requests.get("https://fmpcloud.io/api/v3/historical-price-full/" + ticker + "?from=" + start_date + "&to=" + end_date + "2&apikey=demo")
	data = json.loads(data.content)
	data = data['historical']

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

	return df