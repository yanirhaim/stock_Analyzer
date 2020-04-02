def sma_status(df, ma1, ma2):
    df['50 Daily - SMA'] = df['Close'].rolling(window=ma1).mean()  # moving average 6
    df['200 Daily - SMA'] = df['Close'].rolling(window=ma2).mean()  # moving average 12
    df['Position'] = df['50 Daily - SMA'] > df['200 Daily - SMA']  # look the position between the SMA50 and SMA20

    cut_up = (df['Position'].shift(1) == False) & (df['Position'] == True)  # Places where the SMAs cut UP
    cut_down = (df['Position'].shift(1) == True) & (df['Position'] == False)  # Places where the SMAs cut DOWN

    if df['Position'][-1]:
        status = "UPWARD TREND"
    else:
        status = "DOWNWARD TREND"

    return status
