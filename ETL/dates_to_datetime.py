import pandas as pd
def dates_to_datetime(df):
    df['Created Date'] = pd.to_datetime(df['Created Date'], errors='coerce', format="%m/%d/%Y %I:%M:%S %p")
    df['Closed Date'] = pd.to_datetime(df['Closed Date'], errors='coerce', format="%m/%d/%Y %I:%M:%S %p")
    print('==>Casting dates as datetime format')
    return df