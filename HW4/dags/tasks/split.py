import pandas as pd
from sklearn.model_selection import train_test_split

def split():
    df = pd.read_csv("/opt/airflow/data/convert_sentiment.csv", converters={"tokens": eval})
    train, test = train_test_split(df, test_size=0.2, random_state=1, stratify=df["sentiment"])
    train.to_csv("/opt/airflow/data/train.csv", index=False)
    test.to_csv("/opt/airflow/data/test.csv", index=False)