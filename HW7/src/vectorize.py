import pandas as pd
import sys
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

inp, x_out = sys.argv[1], sys.argv[2]
df = pd.read_csv(inp)

df['StemmatizedReview'] = df['StemmatizedReview'].apply(lambda x: " ".join(eval(x)) if isinstance(x, str) else "")

count_vectorizer = CountVectorizer(ngram_range=(1,2), max_features=5000)
X = count_vectorizer.fit_transform(df['StemmatizedReview'])

np.save(x_out, X.toarray())