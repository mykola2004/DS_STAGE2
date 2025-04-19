import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")

def remove_stopwords():
    stop_words = set(stopwords.words("english"))
    df = pd.read_csv("/opt/airflow/data/tokenize_reviews.csv", converters={"tokens": eval})
    df["tokens"] = df["tokens"].apply(lambda tokens: [word for word in tokens if word not in stop_words])
    df.to_csv("/opt/airflow/data/remove_stopwords.csv", index=False)