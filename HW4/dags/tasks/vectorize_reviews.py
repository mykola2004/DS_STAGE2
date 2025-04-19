import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def vectorize_reviews():
    train = pd.read_csv("/opt/airflow/data/train.csv", converters={"tokens": eval})
    test  = pd.read_csv("/opt/airflow/data/test.csv" , converters={"tokens": eval})

    train["joined"] = train["tokens"].apply(lambda tokens: " ".join(tokens))
    test ["joined"] = test ["tokens"].apply(lambda tokens: " ".join(tokens))

    vectorizer = CountVectorizer(max_features=2000)
    X_train    = vectorizer.fit_transform(train["joined"])
    X_test     = vectorizer.transform(test["joined"])

    df_train = pd.DataFrame(X_train.toarray(), columns=vectorizer.get_feature_names_out())
    df_test  = pd.DataFrame(X_test.toarray() , columns=vectorizer.get_feature_names_out())

    df_train["sentiment"] = train["sentiment"].values
    df_test["sentiment"]  = test["sentiment"].values

    df_train.to_csv("/opt/airflow/data/train_vectorized.csv", index=False)
    df_test.to_csv("/opt/airflow/data/test_vectorized.csv"  , index=False)