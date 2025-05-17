import pandas as pd
import re
import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

inp, out = sys.argv[1], sys.argv[2]
df = pd.read_csv(inp)

def clean_review(text):
    text = str(text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\W+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.lower().strip()

def tokenize_review(review_text):
    return word_tokenize(review_text)

stop_words = set(stopwords.words('english'))
def remove_stopwords(tokenized_text):
    return [token for token in tokenized_text if token not in stop_words]

df = df.drop_duplicates()

df['review'] = df['review'].apply(clean_review)

df['review'] = df['review'].apply(tokenize_review)

df['review'] = df['review'].apply(remove_stopwords)

df.to_csv(out, index=False)