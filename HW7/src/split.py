import pandas as pd
import numpy as np
import sys
from sklearn.model_selection import train_test_split

inp_csv, inp_X, train_out, test_out = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
df = pd.read_csv(inp_csv)
X = np.load(inp_X)

df['sentiment'] = df['sentiment'].map({"positive": 1, "negative": 0})

X_train, X_test, y_train, y_test = train_test_split(X, df['sentiment'], test_size=0.2, random_state=1, stratify=df['sentiment'])

np.savez(train_out, X=X_train, y=y_train)
np.savez(test_out, X=X_test, y=y_test)