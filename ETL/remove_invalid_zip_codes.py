import pandas as pd


def remove_invalid_zip_codes(df: pd.DataFrame) -> pd.DataFrame:
    df["Incident Zip"] = df["Incident Zip"].str.strip()
    isnum = df["Incident Zip"].str.isnumeric()
    islength5 = df["Incident Zip"].str.len() == 5
    iscorrectrange = df["Incident Zip"].astype(float).between(501, 99950)
    condition = isnum & islength5 & iscorrectrange
    if df[~condition]["Incident Zip"].shape[0] != 0:
        print(
            f"==>Step check zip codes: removed incident zip codes {df[~condition]['Incident Zip'].unique()}"
        )
    else:
        print("==>No removed Incident zip codes")
    df = df[condition]
    return df
