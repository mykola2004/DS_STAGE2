import pandas as pd

def merge():
    df1 = pd.read_csv("/opt/airflow/data/datasetp1.csv")
    df2 = pd.read_csv("/opt/airflow/data/datasetp2.csv")
    df  = pd.concat([df1, df2], ignore_index=True)
    df.to_csv("/opt/airflow/data/merged.csv", index=False)