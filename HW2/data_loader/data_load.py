import pandas as pd

filepath = "/app/data/iris.csv"

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
df.to_csv(filepath, index=False)

print("Loaded data")