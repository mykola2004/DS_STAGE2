import transformers
import torch
import pandas as pd
import sklearn

print("Hello!0")

pathway = "../data/train.csv"

df = pd.read_csv(pathway)

print(df.head())