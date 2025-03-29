import transformers as transf
import torch as trch
import pandas as pd
import sklearn as skl

print("Hello World!")

pathway = "../data/train.csv"
df = pd.read_csv(pathway)

print(df.head())

print("It works!")