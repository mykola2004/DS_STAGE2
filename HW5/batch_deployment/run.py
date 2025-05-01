import pandas as pd
import os
from project_package.model import predict

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_CSV = os.path.join(CURRENT_DIR, "input.csv")
OUTPUT_CSV = os.path.join(CURRENT_DIR, "output.csv")

df = pd.read_csv(INPUT_CSV)

df["prediction"] = df.apply(lambda row: predict(row.tolist()), axis=1)

df.to_csv(OUTPUT_CSV, index=False)