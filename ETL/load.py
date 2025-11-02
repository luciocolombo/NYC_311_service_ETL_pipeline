#The dataset is very big and pandas has trouble assigning dtypes to the columns automatically because of bad data quality. We assign dtype=str and cast manually.
import os
import pandas as pd
def load(rows):
    print('Loaded sample of the total dataset, with some of the total columns only')
    data_path = os.getenv("DATA_PATH", "./311_Service_Requests_from_2010_to_Present.csv") #prevents Github CI to break when no dataset is in remote repository. Use sample instead.
    return pd.read_csv(data_path, dtype=str, nrows=rows, 
        usecols = [
            "Unique Key",
            "Created Date",
            "Closed Date",
            "Agency",
            "Agency Name",
            "Complaint Type",
            "Descriptor",
            "Location Type",
            "Incident Zip",
            "Incident Address",
            "Borough",
            "Status",
            "Bridge Highway Direction",
            "Taxi Company Borough",
            "Vehicle Type",
            "School or Citywide Complaint",
            "Intersection Street 1",
            "Ferry Direction",
            "Ferry Terminal Name",
            "Bridge Highway Segment",
            "Taxi Pick Up Location",
            "Bridge Highway Name",
            "Garage Lot Name",
            "Intersection Street 2",
            "Road Ramp",
            "Landmark"
        ]

    )
    
