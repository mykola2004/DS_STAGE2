import pandas as pd
import numpy as np
import sys
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score

train_path, test_path, metrics_path = sys.argv[1], sys.argv[2], sys.argv[3]

train = np.load(train_path)
test = np.load(test_path)
X_train, y_train = train['X'], train['y']
X_test, y_test = test['X'], test['y']

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

metrics_df = pd.DataFrame([{"accuracy": acc, "f1_score": f1}])
metrics_df.to_csv(metrics_path, index=False)