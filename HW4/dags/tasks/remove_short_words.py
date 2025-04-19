import pandas as pd

def remove_short_words():
    df = pd.read_csv("/opt/airflow/data/stem_tokens.csv", converters={"tokens": eval})
    df["tokens"] = df["tokens"].apply(lambda tokens: [word for word in tokens if len(word) > 2])
    df.to_csv("/opt/airflow/data/remove_short_words.csv", index=False)