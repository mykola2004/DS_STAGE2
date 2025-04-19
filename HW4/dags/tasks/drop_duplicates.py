import pandas as pd

def drop_duplicates():
    df = pd.read_csv("/opt/airflow/data/merged.csv")
    df.drop_duplicates(inplace=True)
    df.to_csv("/opt/airflow/data/drop_duplicates.csv", index=False)
