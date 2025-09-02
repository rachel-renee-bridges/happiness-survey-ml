import pandas as pd

# Load the ACME Happiness Survey 2020 CSV file from 01_data/01_raw
def load_acme_data():
    df = pd.read_csv("01_data/01_raw/ACME-HappinessSurvey2020.csv")
    return df

