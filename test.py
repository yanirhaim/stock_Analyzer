from stock_data import get_stock
from indicators.rsiP import rsi_status

df = get_stock('AAPL')
print(df)
print(rsi_status(df, 14))