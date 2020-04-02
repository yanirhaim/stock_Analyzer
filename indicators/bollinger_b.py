def bollinger_b_status(df, period):
    # Calculating the 30 Day Moving Average
    df['30 Day MA'] = df['adjClose'].rolling(window=period).mean()

    # Calculating the 30 Day Standard Deviation
    df['30 Day STD'] = df['adjClose'].rolling(window=period).std()

    # Creating Upper and Lowe Bands
    df['Upper Band'] = df['30 Day MA'] + (df['30 Day STD'] * 2)
    df['Lower Band'] = df['30 Day MA'] - (df['30 Day STD'] * 2)


