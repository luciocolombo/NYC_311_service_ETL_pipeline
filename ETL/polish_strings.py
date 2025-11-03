import pandas as pd


def polish_strings(df: pd.DataFrame) -> pd.DataFrame:
    for col in [
        "Borough",
        "Agency",
        "Agency Name",
        "Complaint Type",
        "Descriptor",
        "Location Type",
        "Incident Address",
    ]:
        df[col] = df[col].astype(str).str.strip().str.lower()
    print("==>All string columns have been standarized")
    return df
