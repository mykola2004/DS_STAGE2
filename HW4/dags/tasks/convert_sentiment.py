import pandas as pd

def convert_sentiment():
    df = pd.read_csv("/opt/airflow/data/remove_short_words.csv", converters={"tokens": eval})
    df["sentiment"] = df["sentiment"].map({"positive": 1, "negative": 0})
    df.to_csv("/opt/airflow/data/convert_sentiment.csv", index=False)