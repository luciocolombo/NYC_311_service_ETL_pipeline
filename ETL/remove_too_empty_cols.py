import pandas as pd


def remove_too_empty_cols(
    df: pd.DataFrame, max_nulls_percentage: float
) -> pd.DataFrame:
    ds = df.dropna(axis=1, thresh=int(max_nulls_percentage * len(df)))
    difference = set(df.columns) - set(ds.columns)
    if len(difference) != 0:
        print(f"==>Removing too empty columns: removed {difference}")
    else:
        print("==>No too empty columns to remove")
    return ds
