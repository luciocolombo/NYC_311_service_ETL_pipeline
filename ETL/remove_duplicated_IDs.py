import pandas as pd


def remove_duplicated_IDs(df: pd.DataFrame) -> pd.DataFrame:
    ds = df.drop_duplicates(subset=["Unique Key"])
    set_difference = set(ds["Unique Key"]) - set(df["Unique Key"])
    if len(set_difference) != 0:
        print(f"==>Removing duplicated keys IDs: {set_difference}")
    else:
        print("==>No duplicated IDs to remove")
    return ds
