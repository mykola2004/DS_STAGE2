import pandas as pd
import re

def clean_review(text):
    text = str(text)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\W+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.lower().strip()

def clean_reviews():
    df = pd.read_csv("/opt/airflow/data/drop_duplicates.csv")
    df["review"] = df["review"].apply(clean_review)
    df.to_csv("/opt/airflow/data/clean_reviews.csv", index=False)

