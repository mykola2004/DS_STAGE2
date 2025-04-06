
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

X, y = load_breast_cancer(return_X_y=True, as_frame=True)
X = X[['mean radius', 'mean texture', 'mean perimeter', 'mean area']]

model = LogisticRegression(max_iter=100)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
model.fit(X_train, y_train)
acc = accuracy_score(y_test, model.predict(X_test))
print("Reproduced accuracy:", acc)
