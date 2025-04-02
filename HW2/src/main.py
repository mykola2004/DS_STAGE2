import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier

print("Loading data")
filepath = "/app/data/iris.csv"
df = pd.read_csv(filepath)

print("Creating test and train sets")
X = df.drop("species", axis=1)
y = df["species"]

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=1)

print("Training XGBoost classifier")
model = XGBClassifier()
model.fit(X_train, y_train)

print("Calculating accuracy")
preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

print(f"Model accuracy: {acc:.4f}")