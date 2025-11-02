import pandera as pa
from pandera import Column, Check
def final_validation(df): #Superior validation over asserts implemented in final_validation
    schema = pa.DataFrameSchema({
        "Unique Key": Column(str, unique=True, nullable=False),
        "Created Date": Column(pa.DateTime),
        "Closed Date": Column(pa.DateTime, nullable=True),
        "Agency": Column(str, nullable=True),
        "Agency Name": Column(str, nullable=True),
        "Complaint Type": Column(str, nullable=True),
        "Descriptor": Column(str, nullable=False),
        "Location Type": Column(str, nullable=True),
        "Incident Zip": Column(str, Check.str_matches(r"^\d{5}$"), nullable=True),
        "Incident Address": Column(str, nullable=True),
        "Borough": Column(str, Check.isin(["bronx","brooklyn","manhattan","queens","staten island"]), nullable=True),
        "Status": Column(str, Check.isin(["closed","open","assigned"]), nullable=False),
    })
    schema.validate(df, lazy=True)
    print("==> Correct schema validation with Pandera. Checked nullability, data types, categorical values, and unique IDs.")
    return df



    
#def final_validation_legacy(df): #Version is surpassed by pandera implementation
#    assert df['Unique Key'].duplicated().sum() == 0, 'Duplicated ID'
#    assert df['Created Date'].dtype == 'datetime64[ns]', 'Created Date is not a date'
#    assert df['Closed Date'].dtype == 'datetime64[ns]', 'Closed Date is not a date'
#    assert df['Status'].isin(['closed','open','assigned']).all(), 'Unrecognized status'
#    print('==>All validations passed')
#    return df

