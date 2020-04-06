import numpy as np

def rsi_percent(df, period):
    period = period  # Value of the RSI period

    # Creating a function where it will store the value of change per day, but just the ones that are increasing on a df
    def upward_c(close_p):
        mask = (close_p - close_p.shift(1)) > 0  # Condition for looking just increasing change per day
        v1 = close_p - close_p.shift(1)  # In case it is increasing it will store this value
        v2 = 0  # In case it is not increasing it will store this value
        df['Upward change'] = np.where(mask, v1, v2)  # Assigning the condition to the df, to assign the values

    upward_c(df['Close'])  # Calling the function with the Close Values

    # Creating a function where it will store the value of change per day, but just the ones that are decreasing on a df
    def downward_c(close_p):
        mask = (close_p - close_p.shift(1)) < 0  # Condition for looking just decreasing change per day
        v1 = (close_p - close_p.shift(1)) * -1  # In case it is decreasing it will store this value
        v2 = 0  # In case it is not decreasing it will store this value
        df['Downward change'] = np.where(mask, v1, v2)  # Assigning the condition to the df, to assign the values

    downward_c(df['Close'])  # Calling the function with the Close Values

    # Creating a function where it return an average change in relationship with the period, returning a list of values
    def av_m(change):
        x = 1
        y = 0
        f_value = 0
        avm = []
        while y != period:
            avm.append(np.nan)
            y += 1
        while x != period + 1:
            f_value += change[x]
            x += 1
        f_value = f_value / period
        avm.append(f_value)
        for up_ch in change[period + 1:]:
            avm.append(((f_value * (period - 1)) + up_ch) / period)
            f_value = ((f_value * (period - 1)) + up_ch) / period
        return avm

    df['Average UM'] = av_m(df['Upward change'])  # Getting the average upward movement values and storing them on a df
    df['Average DM'] = av_m(df['Downward change'])  # Getting the average downward movement values and storing them on a
                                                    # df

    df['RS'] = df['Average UM'] / df['Average DM']  # Getting the Relative Strength, and storing the values on a df

    # Function to obtain the Relative Strength index from the RS values, and returning a list.
    def rsi(rs):
        x = 0
        rsi_l = []
        while x != period:
            rsi_l.append(np.nan)
            x += 1
        for val in rs[period:]:
            rsi_l.append(100 - (100 / (val + 1)))

        return rsi_l

    df['RSI'] = rsi(df['RS'])  # Storing the list of values of the RSI on a df

    def b_percentage(value):
        percentage = []
        for item in df['RSI']:
            if item > 70:
                percentage.append(100)
            elif item < 30:
                percentage.append(0)
            else:
                value = ((item-30)*10)/4
                percentage.append(100 - round(float(value),2))
        return percentage

    return b_percentage(df['RSI'])[-1] # Calling the function to get the percentage for buying
