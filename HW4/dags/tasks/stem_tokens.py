import pandas as pd
import nltk
from nltk.stem import PorterStemmer
nltk.download("punkt")

def stem_tokens():
    stemmer = PorterStemmer()
    df = pd.read_csv("/opt/airflow/data/remove_stopwords.csv", converters={"tokens": eval})
    df["tokens"] = df["tokens"].apply(lambda tokens: [stemmer.stem(word) for word in tokens])
    df.to_csv("/opt/airflow/data/stem_tokens.csv", index=False)