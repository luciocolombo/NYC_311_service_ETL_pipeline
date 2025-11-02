import pandas as pd
def remove_invalid_status(df):
    df.Status = df.Status.str.strip().str.lower()
    mask = df.Status.isin(['closed', 'open', 'assigned'])
    if df[~mask].shape[0] != 0:
        print(f'==>Step Status check: Removed {df[~mask].shape[0]}')
    else:
        print('==>No invalid status to remove')
    return df[mask]

    
    