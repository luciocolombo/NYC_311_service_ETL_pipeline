import pandas as pd
def remove_too_empty_cols(df, max_nulls):
    ds = df.dropna(axis=1, thresh=max_nulls*len(df))
    difference = set(df.columns)-set(ds.columns)
    if len(difference) != 0:
        print(f'==>Removing too empty columns: removed {difference}')
    else:
        print('==>No too empty columns to remove')
    return ds