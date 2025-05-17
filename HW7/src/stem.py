import pandas as pd
import sys
from nltk.stem import PorterStemmer
import nltk
import ast

nltk.download('punkt')
nltk.download('stopwords')

inp, out = sys.argv[1], sys.argv[2]
df = pd.read_csv(inp)

stemmer = PorterStemmer()
def apply_stemming(tokens):
    return [stemmer.stem(token) for token in tokens]

def remove_short_words(tokens):
    return [token for token in tokens if len(token) > 2]

df['review'] = df['review'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

df['StemmatizedReview'] = df['review'].apply(apply_stemming)
df['StemmatizedReview'] = df['StemmatizedReview'].apply(remove_short_words)
df.to_csv(out, index=False)