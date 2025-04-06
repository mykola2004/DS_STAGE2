import json
import sys
import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
import random
import os
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import ConfusionMatrixDisplay

MODELS = {
    "LogisticRegression": LogisticRegression,
    "RandomForestClassifier": RandomForestClassifier,
    "KNeighborsClassifier": KNeighborsClassifier
}

def run_model(config_path):
    with open(config_path, "r") as f:
        config = json.load(f)

    random_state = config["random_state"]
    random.seed(random_state)
    np.random.seed(random_state)

    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)[config["features"]]
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)

    model_class = MODELS[config["model"]]
    model = model_class(**config["params"])
    if "random_state" in model.get_params():
        model.set_params(random_state=random_state)

    mlflow.set_tracking_uri("http://mlflow:5000")
    mlflow.set_experiment("Breast Cancer Classification")

    with mlflow.start_run():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        mlflow.log_params(config["params"])
        mlflow.log_param("model", config["model"])
        mlflow.log_param("features_used", ",".join(config["features"]))
        mlflow.log_param("random_state", random_state)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, artifact_path="model")

        plt.bar(["accuracy"], [acc])
        plt.ylim(0, 1)
        plt.title(f"{config['model']} acc={acc:.2f}")
        plt.savefig("Accuracy_plot.png")
        mlflow.log_artifact("Accuracy_plot.png")
        plt.close()
        os.remove("Accuracy_plot.png")

        disp = ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
        disp.ax_.set_title("Confusion Matrix")
        plt.savefig("Confusion_matrix.png")
        mlflow.log_artifact("Confusion_matrix.png")
        plt.close()
        os.remove("Confusion_matrix.png")

        TEMPLATE_CODE = f'''
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

X, y = load_breast_cancer(return_X_y=True, as_frame=True)
X = X[{config["features"]}]

model = {config["model"]}({", ".join(f"{parameter}={value}" for parameter,value in config["params"].items())})
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state={config["random_state"]})
model.fit(X_train, y_train)
acc = accuracy_score(y_test, model.predict(X_test))
print("Reproduced accuracy:", acc)
'''

        with open("train_used.py", "w") as f:
            f.write(TEMPLATE_CODE)
        mlflow.log_artifact("train_used.py")
        os.remove("train_used.py")

        mlflow.log_artifact(config_path)

if __name__ == "__main__":
    run_model(sys.argv[1])