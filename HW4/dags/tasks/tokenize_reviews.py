import pandas as pd
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt_tab')

def tokenize_reviews():
    df = pd.read_csv("/opt/airflow/data/clean_reviews.csv")
    df["tokens"] = df["review"].apply(word_tokenize)
    df.to_csv("/opt/airflow/data/tokenize_reviews.csv", index=False)