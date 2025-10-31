
# NYC 311 Service Requests – ETL Pipeline (Pipe/Prefect)

## Overview
A lightweight and reproducible ETL pipeline built in Python to clean and standardize the **NYC 311 Service Requests** dataset.
The project focuses on clarity, validation through assertions, and readable transformations — aligned with a data analyst workflow.

## Branches

This repository contains two versions of the ETL pipeline:

| Branch | Description |
|---------|--------------|
| **`master`** | Standard Pandas pipeline using `DataFrame.pipe()` — focuses on clarity and functional chaining inside a notebook. |
| **`prefect`** | Alternative orchestration using **Prefect**. Each ETL step is defined as a `@task` within a `@flow`, enabling retries, logging, and execution control. Useful for production-style automation. |

Both branches produce the same final dataset.  
The Prefect version adds scheduling and observability features for workflow orchestration.

## CI (Github actions)

Each push triggers a GitHub Actions pipeline that runs the ETL notebook with pytest + nbmake.
It ensures all Pandera checks and assertions pass in a clean environment (and runs Prefect flows on the prefect branch).


## Data Source
**Dataset:** [Kaggle – 311 Service Requests NYC](https://www.kaggle.com/datasets/pablomonleon/311-service-requests-nyc)

To reproduce locally:
```
kaggle datasets download -d pablomonleon/311-service-requests-nyc -p data/ --unzip
```
A small sample is included in the repository (this is not the full dataset)
The notebook reads the raw CSV from the `data/` folder.
The raw file should not be uploaded to the repository due to its size.


## Dataset Summary
The raw dataset contains **364,558 rows** and **53 columns**, representing 311 service requests filed by NYC residents.  
In this project, a configurable sample of **20,000 rows** is used for faster, reproducible ETL testing.

| Feature type | Example columns | Notes |
|---------------|----------------|-------|
| **Identifiers** | `Unique Key` | Unique ticket ID for each request |
| **Dates** | `Created Date`, `Closed Date`, `Due Date`, `Resolution Action Updated Date` | Stored as strings, later converted to `datetime` |
| **Agency information** | `Agency`, `Agency Name` | Department responsible for the complaint |
| **Complaint details** | `Complaint Type`, `Descriptor`, `Status` | Main categorical variables for analysis |
| **Location** | `Incident Zip`, `City`, `Borough`, `Latitude`, `Longitude` | Used for spatial validation and filtering |
| **Address details** | `Incident Address`, `Street Name`, `Cross Street 1`, `Cross Street 2` | Often partially missing |
| **Education / Parks fields** | `School Name`, `Park Facility Name`, `School Region`, etc. | Usually constant or irrelevant for most analyses |
| **Sparse fields** | `Vehicle Type`, `Bridge Highway Name`, `Ferry Terminal Name` | Contain mostly null values |


## Pipeline Structure

The notebook defines clear modular functions and uses `DataFrame.pipe()` for a clean flow.

1. **`load(rows)`**
   Loads a sample of the dataset (`dtype=str`, `nrows=rows`) with selected columns.
   Prints basic information about the data loaded.

2. **`remove_too_empty_cols(df, max_nulls)`**
   Drops columns exceeding a missing value threshold (`max_nulls`).
   Logs which columns were removed or confirms no change.

3. **`remove_duplicated_IDs(df)`**
   Removes duplicate tickets based on the unique complaint ID.
   Prints number of duplicates removed.

4. **`dates_to_datetime(df)`**
   Converts date columns to `datetime` using an explicit format to prevent parsing warnings.

5. **`remove_invalid_zip_codes(df)`**
   Filters out rows with invalid ZIP codes and logs how many were removed.

6. **`remove_invalid_status(df)`**
   Filters out invalid status values based on a predefined domain.
   Prints counts of filtered records.

7. **`polish_strings(df)`**
   Normalizes text columns (trims whitespace, fixes casing).

8. **`final_validation(df)`**
   Runs final `assert` checks for integrity.
   Example rules:

   -  No null IDs
   -  No duplicate IDs
   -  Valid date conversion

9. **`main()`**
   Starts a timer with `time.time()`.
   Runs the entire pipeline using `.pipe()` and prints the total duration:

   ```
   Your data is ready, processed in <seconds>, resulting in <rows> rows and <cols> columns
   ```

## Usage

Open the notebook `311_NYC_Service_Complaints_ETL.ipynb` and run:

```python
main()
```

Editable parameters:

-  `load(20000)` to change the sample size
-  `max_nulls` in `remove_too_empty_cols()` to adjust threshold

## Output

The final cleaned DataFrame is kept in memory after running `main()`.
If you wish to export it, append this line:

```python
df.to_csv("311_clean.csv", index=False)
```

This produces a clean CSV ready for analysis.

## Technical Notes

-  Reads with `dtype=str` to prevent type inference errors
-  Uses `DataFrame.pipe()` for modular readability
-  Validation handled through `assert` statements with clear messages
-  Measures runtime using `time.time()` for transparency

## Example Console Output
(This is not exactly what is outputed)
```
Loaded 20000 rows
Removed 2 duplicated IDs
Converted dates successfully
Cleaned 311 data in 4.82s
Your data is ready, processed in 4.82s, resulting in 18456 rows and 12 columns
```

## Project Type

**Category:** Data Cleaning / ETL
**Language:** Python (Pandas)
**Focus:** Real-world dataset transformation for analytics
